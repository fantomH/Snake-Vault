# :: --------------------------------------------------------------------- INFO
# :: [snake_vault/snake_sqlite/xml2sqlite.py]
# :: author        : Pascal Malouin @ github.com/fantomH
# :: created       : 2025-09-23 13:11:49 UTC
# :: updated       : 2025-09-23 13:11:53 UTC
# :: description   : Import xml data to SQLite table.

"""
Import xml data to SQLite table.
"""

import argparse
import re
import sqlite3
from collections import Counter
from typing import Dict, List, Tuple, Optional

from lxml import etree as ET

def localname(tag: str) -> str:
    # :: "{uri}Name" -> "Name"   or  "Name" -> "Name"
    return tag.split('}')[-1] if '}' in tag else tag

def to_snake(name: str) -> str:
    """
    Nomalize a string into a safe SQL identifier.

    - Strip XML namespace.
    - Replace any char not in [0-9A-Za-z_] with '_'.
    - Prefix with '_' if it starts with a digit.

    Examples:
        to_snake("{http://x.org}Exam.Service-Item") -> "Exam_Service_Item"
        to_snake("123Name") -> "_123Name"
    """

    name = localname(name)
    name = re.sub(r'[^0-9A-Za-z_]+', '_', name)
    if re.match(r'^\d', name):
        name = '_' + name
    return name

def value_from_elem(e: ET._Element) -> Optional[str]:
    """
    Get the element's text (and handles nil).
    """

    # Handle xsi:nil="true"
    for k, v in e.attrib.items():
        if localname(k) == 'nil' and str(v).lower() == 'true':
            return None
    # Trim text; treat empty as None
    txt = (e.text or '').strip()
    return txt if txt != '' else None

def ensure_table(conn: sqlite3.Connection, table: str, cols: List[str]) -> None:
    """
    - Create table if it does not exist.
    - Add missing columns.
    """

    cur = conn.execute(f'PRAGMA table_info("{table}")')
    existing = {row[1] for row in cur.fetchall()}
    if not existing:
        cols_def = ", ".join(f'"{c}" TEXT' for c in cols)
        conn.execute(f'CREATE TABLE "{table}" ({cols_def})')
        return
    missing = [c for c in cols if c not in existing]
    for c in missing:
        conn.execute(f'ALTER TABLE "{table}" ADD COLUMN "{c}" TEXT')

def insert_batch(
    conn: sqlite3.Connection,
    table: str,
    rows: List[Dict[str, Optional[str]]]
    ) -> None:

    if not rows:
        return
    cols = sorted({c for r in rows for c in r.keys()})
    ensure_table(conn, table, cols)
    placeholders = ",".join(["?"]*len(cols))
    sql = f'INSERT INTO "{table}" ({",".join(f"""\"{c}\"""" for c in cols)}) VALUES ({placeholders})'
    vals = [tuple(r.get(c) for c in cols) for r in rows]
    conn.executemany(sql, vals)

def detect_element(xml_path: str, max_probe: int = 1000) -> str:
    """
    Streaming detection of the most common element directly under the root.

    Scans the XML with iterparse (start events), counts the local names of
    direct children of the root, and returns the most frequent one. This is
    assumed to be the repeating "record" element.

    Args:
        xml_path (str): Path to the XML file.
        max_probe (int, optional): Maximum number of first-level children to sample.
                                   Defaults to 1000.

    Returns:
        str: The detected element's localname (namespace stripped).

    Raises:
        SystemExit: If no suitable element is found or the detected name is 'schema'.
    """

    # Track the root element and counts of its direct children
    root: Optional[ET._Element] = None
    counts: Counter[str] = Counter()
    probed = 0

    # We use start events to avoid building the whole tree.
    for event, elem in ET.iterparse(xml_path, events=("start",)):
        if root is None:
            # First start event is the root
            root = elem
            continue

        # Direct child if parent is root (lxml supports .getparent())
        if elem.getparent() is root:
            tag = elem.tag
            # localname: "{uri}Name" -> "Name"
            lname = tag.split('}')[-1] if '}' in tag else tag
            counts[lname] += 1
            probed += 1
            if probed >= max_probe:
                break

    if not counts:
        raise SystemExit(f"Could not auto-detect record element in {xml_path}. Use --element.")

    element = counts.most_common(1)[0][0]
    if element.lower() == "schema":
        raise SystemExit(f"No proper value detected (got 'schema'). Skipping {xml_path}")

    return element

def import_xml(
    xml_path: str,
    db_path: str,
    table: str,
    element_local: str | None = None,
    batch_size: int=1000,
    drop_existing: bool=False,
    ) -> None:
    """
    Stream-parse an XML file and insert rows into a SQLite table in batches.

    If `element_local` is None, auto-detect the record element with `detect_element`.
    Rows are inserted in batches of `batch_size` using `insert_batch`. The function
    applies fast SQLite PRAGMAs optimized for ETL workloads (reduced durability).

    Args:
        xml_path (str): Path to the XML file to import.
        db_path (str): Path to the destination SQLite database file.
        table (str): Destination table name.
        element_local (str | None): Local name of the repeating record element;
            if None, it will be auto-detected.
        batch_size (int): Number of rows per batch insert (default: 1000).
        drop_existing (bool): If True, drop the destination table/view before importing.
    """

    with sqlite3.connect(db_path) as conn:

        if element_local is None:
            element_local = detect_element(xml_path)

        # :: Fast Pragmas.
        conn.execute("PRAGMA journal_mode=WAL;")
        conn.execute("PRAGMA synchronous=OFF;")
        conn.execute("PRAGMA temp_store=MEMORY;")
        conn.execute("PRAGMA cache_size=-200000;")  # ~200MB negative = KB units

        # :: Drop table if --drop-existing
        if drop_existing:
            conn.execute(f'DROP TABLE IF EXISTS "{table}"')
            conn.execute(f'DROP VIEW IF EXISTS "{table}"')
            conn.commit()

        batch: List[Dict[str, Optional[str]]] = []

        context = ET.iterparse(xml_path, events=("end",))
        for _, elem in context:
            if localname(elem.tag) != element_local:
                continue

            row: Dict[str, Optional[str]] = {}
            for child in elem:
                key = to_snake(child.tag)
                row[key] = value_from_elem(child)

            batch.append(row)

            if len(batch) >= batch_size:
                insert_batch(conn, table, batch)
                conn.commit()
                batch.clear()

            # :: free memory
            elem.clear()
            parent = elem.getparent()
            if parent is not None:
                while parent.getprevious() is not None:
                    # :: drop processed siblings to keep memory flat.
                    gp = parent.getparent()
                    if gp is not None:
                        del gp[0]
                    else:
                        break

        # :: final flush
        insert_batch(conn, table, batch)
        conn.commit()
