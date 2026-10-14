def read_rows(lines):
    header = None
    rows = []

    for line in lines:
        line = line.strip()
        if not line: continue
        parts = [p.strip() for p in line.split(',')]
        if header is None: header = parts
        elif len(parts) == len(header): rows.append(dict(zip(header, parts)))

    return rows


def count_types(rows):
    counts = {}
    for row in rows:
        temp = row['тип']
        counts[temp] = counts.get(temp, 0) + 1
    return counts

def total_minutes(rows, kind):
    total = 0.0
    for row in rows:
        if kind == row['тип']:
            val = row['минуты'].replace(',', '.')
            try:
                total += float(val)
            except ValueError as val_err:
                print(f"Ошибка: {val_err}")
                continue
    return round(total, 1)

def to_csv(counts):
    lines = ['тип,количество']
    for kind in sorted(counts):
        lines.append(f"{kind},{counts[kind]}")
    return '\n'.join(lines) + '\n'
