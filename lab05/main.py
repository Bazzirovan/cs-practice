from tablestats import *

fn = input().strip()

with open(fn, encoding = 'utf-8') as f:
    rows = read_rows(f)

counts = count_types(rows)

print(len(rows))
print(len(counts))
print(total_minutes(rows, 'ошибка'))



with open("summary.csv", "w", encoding="utf-8") as out:
    out.write(to_csv(counts))
