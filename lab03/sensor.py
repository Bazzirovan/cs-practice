threshold = float(input("Укажите порог: "))
n = int(input("Укажите количество строк: "))

total = 0
errors = 0

for _ in range(n):
    line = input().strip()
    total += 1
    if line == "error":
        errors += 1
        continue
    line = float(line)

print(total)
print(errors)
