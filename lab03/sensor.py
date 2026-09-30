threshold = float(input("Укажите порог: "))
n = int(input("Укажите количество строк: "))
total = 0

for _ in range(n):
    line = input().strip()
    total += 1

print(total)
