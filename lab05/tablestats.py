def read_rows(lines):
    header = None
    rows = []

    for line in lines:
        line = line.strip()
        if not line: continue
        parts = [p.strip()] for p in line.split(',')
        if header is None: header = parts
        elif len(parts) == len(header): rows.append(dict(zip(header, parts)))

    return rows


def count_types(rows):
    counts = {}
    for row in rows:
        temp = row('тип')
        counts[temp] = counts.get(t, 0) + 1
    return counts
