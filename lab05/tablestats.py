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
