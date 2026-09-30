threshold = float(input("Укажите порог: "))
n = int(input("Укажите количество строк: "))

total = 0
errors = 0
max_value = float("-inf")
valid_values = 0
sum_values = 0

for _ in range(n):
    line = input().strip()
    total += 1
    if line == "error":
        errors += 1
        continue
    value = float(line)
    if value > max_value: max_value = value
    if value > threshold: valid_values += 1
    sum_values += value

print(total)
print(errors)
print(valid_values)
print(f"{max_value:.1f}")
print(f"{sum_values/(total-errors):.1f}")
