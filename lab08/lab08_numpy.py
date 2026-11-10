import numpy as np

# task 1
hours = np.arange(0, 22, 3)
line = np.linspace(0, 1, 5)
zeros = np.zeros(6, dtype=int)
unknown_table = np.full((2, 3), -1)
identity = np.identity(3)

print(f'''
Часы: {hours}
Все Axis: {hours.shape}
Размерность: {hours.ndim}
Количество элементов: {hours.size}
Тип элементов массива: {hours.dtype}
''')


# task 2
print(f'''
3-й элемент: {hours[2]}
Последний элемент: {hours[-1]}
Элементы с индексами 2-5: {hours[2:6]}
Каждый второй элемент: {hours[::2]}
Массив в обратном порядке: {hours[::-1]}
''')


# task 3
temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18],
])

print(f'''
Форма, число измерений и элементов: {temperatures.shape, temperatures.ndim, temperatures.size}
Значение из второй строки и третьего столбца: {temperatures[1, 2]}
Первая строка: {temperatures[0]}
Последний столбец: {temperatures[:, -1]}
Первые две строки без первого столбца: \n{temperatures[:2, 1:]}
Центральный фрагмент 2x2: \n{temperatures[:2, 1:3]}
''')


# task 4
matrix = np.arange(1, 26).reshape(5, 5)

print(f'''
Первые три строки: \n{matrix[:3]}
Форма первых трёх строк: {matrix[:3].shape}
Последние две строки: \n{matrix[-2:]}
Форма последних двух строк: {matrix[-2:].shape}
Первые два столбца: \n{matrix[:, :2]}
Форма первых двух столбцов: {matrix[:, :2].shape}
Фрагмент из строк 1-3 и столбцов 2-4: \n{matrix[0:3, 1:4]}
Форма фрагмента из строк 1-3 и столбцов 2-4: {matrix[0:3, 1:4].shape}
Угловой блок 2x2 в правом нижнем углу: \n{matrix[-2:, -2:]}
Форма углового блока 2x2: {matrix[-2:, -2:].shape}
''')


# task 5
vector = np.array([10, 20, 30, 40, 50])
vector[1:4] = 0

small_matrix = np.arange(1, 10).reshape(3, 3)
small_matrix[0, :] = -1
small_matrix[1:, 1:] = 9

changed_hours = hours.copy()
# Срез без copy() ссылается на исходную память (view). Изменение среза меняет оригинал.
changed_hours[2:5] = 99
changed_hours[::2] = -1

changed_matrix = matrix.copy()
changed_matrix[1, :] = 0
changed_matrix[:, -1] = -1
changed_matrix[1:4, 1:4] = 100

print(f'''
Изменённый hours: \n{changed_hours}
Исходный hours: \n{hours}
Изменённая матрица: \n{changed_matrix}
Исходная матрица: \n{matrix}
''')


# task 6
numbers = np.arange(12)
table = numbers.reshape(3, 4)
transposed = table.T
# reshape(3, 4) работает, так как 3 * 4 == 12 == numbers.size.
# reshape(5, 3) вызовет ошибку: 5 * 3 == 15 != 12.

print(f'''
Форма numbers: {numbers.shape}
Форма table: {table.shape}
Форма transposed: {transposed.shape}
''')