# [+] -------------------------------------------------------------------| INFO
# [/Snake-Vault/snake_vault/snake_flask/example/app/plugins/table_generator.py]
# author        : Pascal Malouin (https://github.com/fantomH)
# created       : 2026-05-25 11:56:28 UTC
# updated       : 2026-05-25 18:05:30 UTC
# description   : Table Generator.

"""
Table Generator is a plugin dynamically generating a searchable, sortable,
paginated HTML table for Flask applications.

Features:
- Pagination
- Global search
- Sortable columns
- Resizable columns
- Drag & drop column reordering
- AJAX-loaded data
- Bootstrap styling

The frontend behavior is handled by:
    /static/snake-table.js

The backend data is provided by:
    TableGenerator.get_data()

The table HTML is injected into templates with:

    {{ table_generator.load() }}
"""

from flask import request
from markupsafe import Markup

class TableGenerator:
    """
    Dynamic table generator for Flask.

    This class:
    - Generates HTML/CSS for a table.
    - Defines table metadata (columns, sorting, searching).
    - Provides backend data retrieval logic.
    - Returns paginated JSON-compatible data.

    Example usage:

        table_generator = TableGenerator(
            table_id="users-table",
            data_url="/admin/users/data/",
            db=db,
            source_table="users",
            columns=[
                {
                    "name": "username",
                    "label": "Username",
                    "sortable": True,
                    "searchable": True,
                },
            ],
        )

    Template:

        {{ table_generator.load() }}
    """

    def __init__(
        self,
        table_id,
        data_url,
        db,
        columns,
        source_table=None,
        default_order_by=None):
        """
        Initialize the table generator.

        Parameters
        ----------
        table_id : str
            Unique HTML ID for the table.

        data_url : str
            AJAX endpoint used by snake-table.js
            to fetch table data.

        db : sqlite3.Connection
            Database connection object.

        columns : list[dict]
            List of column definitions.

            Example:

                {
                    "name": "username",
                    "label": "Username",
                    "sortable": True,
                    "searchable": True,
                    "type": "text",
                }

        source_table : str
            Database table name.

        default_order_by : str
            Default SQL ORDER BY clause.

            Example:
                "username ASC"
        """

        self.table_id = table_id
        self.data_url = data_url
        self.db = db
        self.columns = columns
        self.source_table = source_table
        self.default_order_by = default_order_by

    def load(self):
        """
        Generate and return the HTML for the table.

        Returns
        -------
        markupsafe.Markup
            Safe HTML markup.

        This method:
        - Injects CSS.
        - Builds the table structure.
        - Adds pagination controls.
        - Adds the search input.
        - Loads snake-table.js.
        """

        html = f"""
<style>

    /* [+] Main wrapper                                                      */
    /*     Enables horizontal scrolling if the table becomes too wide.       */
    #{self.table_id} .snake-table-wrapper {{
        width: 100%;
        overflow-x: auto;
    }}

    /* [+] Inner table container                                             */
    #{self.table_id} .snake-table-inner {{
        width: 100%;
    }}

    /* [+] Table cells                                                       */
    /*     Prevents text from stretching columns too wide.                   */
    #{self.table_id} .snake-table-inner th,
    #{self.table_id} .snake-table-inner td {{
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
        max-width: 250px;
    }}

    /* [+] Header cells                                                      */
    /*     Needed because resizer handles are absolutely positioned.         */
    #{self.table_id} th {{
        position: relative;
    }}

    /* [+] Column resize handle                                              */
    /*     Small draggable area on the right side of headers.                */
    #{self.table_id} .snake-table-resizer {{
        position: absolute;
        top: 0;
        right: 0;
        width: 6px;
        height: 100%;
        cursor: col-resize;
        user-select: none;
    }}

    /* [+] Drag-and-drop ghost                                               */
    /*     Visual helper while dragging columns.                             */
    .snake-table-drag-ghost {{
        position: fixed;
        pointer-events: none;
        opacity: 1;
        background: white;
        border: 1px solid #111;
        padding: 6px 12px;
        border-radius: 4px;
        z-index: 9999;
    }}

    /* [+] Copyable cells                                                    */
    /* Indicates text cells can be clicked to copy.                          */
    #{self.table_id} .snake-table-copyable {{
        cursor: copy;
    }}
</style>

<!-- [+] Main table container -->
<div
    id="{self.table_id}"
    class="snake-table"
    data-url="{self.data_url}"
>
    <!-- [+] Top controls -->
    <div class="d-flex justify-content-between mb-2">
        <input
            type="text"
            class="form-control w-25 snake-table-search"
            placeholder="Search..."
        >

        <select class="form-select w-auto snake-table-page-size">
            <option value="10">10</option>
            <option value="25" selected>25</option>
            <option value="50">50</option>
            <option value="100">100</option>
        </select>
    </div>

    <!-- [+] Table wrapper -->
    <div class="snake-table-wrapper">
        <table class="table table-striped table-hover align-middle snake-table-inner">
            <thead>
                <tr>
                    {self._render_headers()}
                </tr>
            </thead>
            <tbody></tbody>
        </table>
    </div>

    <!-- [+] Pagination controls -->
    <div class="d-flex justify-content-between align-items-center">
        <button class="btn btn-sm btn-secondary snake-table-prev">Previous</button>
        <span class="snake-table-info"></span>
        <button class="btn btn-sm btn-secondary snake-table-next">Next</button>
    </div>
</div>

<script src="/static/snake-table.js"></script>
"""
        return Markup(html)

    def _render_headers(self):
        """
        Generate the table headers.

        Returns
        -------
        str
            HTML for all <th> elements.

        Each header includes:
        - Drag support
        - Sort metadata
        - Resize handle
        """

        output = ""

        for column in self.columns:
            column_type = column.get("type", "text")
            sortable = "true" if column.get("sortable") else "false"

            output += f"""
<th 
    draggable="true"
    data-column="{column["name"]}"
    data-type="{column_type}"
    data-sortable="{sortable}"
    style="position: relative;"
>
    <!-- Visible column label -->
    {column["label"]}

    <!-- Sort direction indicator -->
    <span class="snake-table-sort-indicator"></span>

    <!-- Resize handle -->
    <span class="snake-table-resizer"></span>
</th>
"""
        return output

    def get_searchable_columns(self):
        """
        Return all searchable columns.

        Returns
        -------
        list[str]

        Example:
            ["username", "email"]
        """

        return [
            column["name"]
            for column in self.columns
            if column.get("searchable")
        ]

    def get_db_columns(self):
        """
        Return columns that exist in the database.

        Some frontend-only columns may exist,
        such as selection checkboxes.

        Example:
            {"name": "selected", "db": False}

        Returns
        -------
        list[str]
        """

        return [
            column["name"]
            for column in self.columns
            if column.get("db", True)
        ]

    def get_select_clause(self):
        """
        Build SQL SELECT clause.

        Example:
            "id, username, email"

        Returns
        -------
        str
        """

        return ", ".join(self.get_db_columns())

    def build_search_where(self, search):
        """
        Build SQL WHERE clause for global search.

        Parameters
        ----------
        search : str
            User search query.

        Returns
        -------
        tuple[str, list]

        Example:

            (
                "WHERE username LIKE ? OR email LIKE ?",
                ["%john%", "%john%"]
            )
        """

        searchable_columns = self.get_searchable_columns()

        # No search or no searchable columns
        if not search or not searchable_columns:
            return "", []

        # Generate LIKE conditions.
        conditions = [
            f"{column} LIKE ?"
            for column in searchable_columns
        ]

        # Build WHERE clause.
        where = f"WHERE {' OR '.join(conditions)}"

        # One parameter per condition.
        params = [f"%{search}%"] * len(searchable_columns)

        return where, params

    def get_sortable_columns(self):
        """
        Return sortable database columns.

        Returns
        -------
        list[str]
        """

        return [
            column["name"]
            for column in self.columns
            if column.get("sortable") and column.get("db", True)
        ]

    def build_order_clause(self, sort_column, sort_direction):
        """
        Return sortable database columns.

        Returns
        -------
        list[str]
        """

        sortable_columns = self.get_sortable_columns()

        # Prevent invalid/non-whitelisted columns.
        if sort_column not in sortable_columns:

            # Use fallback order if configured.
            if self.default_order_by:
                return f"ORDER BY {self.default_order_by}"

            return ""

        # Safety check.
        if sort_direction not in ["asc", "desc"]:
            sort_direction = "asc"

        return f"ORDER BY {sort_column} {sort_direction.upper()}"

    def get_data(self):
        """
        Fetch paginated table data.

        This method is usually called by
        the AJAX data endpoint.

        Returns
        -------
        dict

        Example:
            {
                "rows": [...],
                "page": 1,
                "page_size": 25,
                "total": 500,
            }
        """

        page = int(request.args.get("page", 1))
        page_size = int(request.args.get("page_size", 25))
        search = request.args.get("search", "").strip()
        sort_column = request.args.get("sort_column", "").strip()
        sort_direction = request.args.get("sort_direction", "asc").strip().lower()

        offset = (page - 1) * page_size

        select_clause = self.get_select_clause()
        where, params = self.build_search_where(search)

        order_clause = self.build_order_clause(
            sort_column,
            sort_direction,
        )

        total = self.db.execute(
            f"""
            SELECT COUNT(*)
            FROM {self.source_table}
            {where}
            """,
            params,
        ).fetchone()[0]

        rows = self.db.execute(
            f"""
            SELECT {select_clause}
            FROM {self.source_table}
            {where}
            {order_clause}
            LIMIT ? OFFSET ?
            """,
            params + [page_size, offset],
        ).fetchall()

        return {
            "rows": [dict(row) for row in rows],
            "page": page,
            "page_size": page_size,
            "total": total,
        }
