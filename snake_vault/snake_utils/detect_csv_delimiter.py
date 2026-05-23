# ------------------------------------------------------------------------ INFO
# [/Snake-Vault/snake_vault/snake_utils/detect_csv_delimiter.py]
# author        : Pascal Malouin (https://github.com/fantomH)
# created       : 2026-04-14 12:01:42 UTC
# updated       : 2026-04-14 12:01:42 UTC
# description   : Detect CSV delimiter.

from collections import Counter

def detect_csv_delimiter(file_path, num_lines=10):
    candidates = [',', ';', '|', '\t']
    splits = {c: [] for c in candidates}

    with open(file_path, 'r', encoding='utf-8') as f:
        for _ in range(num_lines):
            line = f.readline()
            if not line:
                break
            for c in candidates:
                splits[c].append(len(line.split(c)))

    scores = {}
    for c, values in splits.items():
        if not values:
            continue

        avg = sum(values) / len(values)
        variance = sum((x - avg) ** 2 for x in values) / len(values)

        scores[c] = (-variance, avg)

        print(f"{c}: {scores[c]}")

    return max(scores, key=scores.get)

def main():

    import sys
    
    if len(sys.argv) != 2:
        print("[!] A unique path required.")
    
    file_path = sys.argv[1]
    delimiter = detect_csv_delimiter(file_path)

    print(f"Detected delimiter: '{delimiter}'")

if __name__ == "__main__":
    main()
