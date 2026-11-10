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


