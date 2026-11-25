import numpy as np


def make_table(rows: int, columns: int) -> list[list[int]]:
    return np.arange(rows * columns).reshape(rows, columns).tolist()


def rectangle(
    matrix: list[list[float]],
    row_start: int,
    row_stop: int,
    column_start: int,
    column_stop: int,
) -> list[list[float]]:
    m = np.asarray(matrix)
    return m[row_start:row_stop, column_start:column_stop].tolist()


def replace_rectangle(
    matrix: list[list[float]],
    row_start: int,
    row_stop: int,
    column_start: int,
    column_stop: int,
    value: float,
) -> list[list[float]]:
    m = np.array(matrix, dtype=float).copy()
    m[row_start:row_stop, column_start:column_stop] = value
    return m.tolist()


def matrix_vector_product(
    matrix: list[list[float]], vector: list[float]
) -> list[float]:
    m = np.asarray(matrix, dtype=float)
    v = np.asarray(vector, dtype=float)
    return (m @ v).tolist()


def matrix_multiply(
    left: list[list[float]], right: list[list[float]]
) -> list[list[float]]:
    a = np.asarray(left, dtype=float)
    b = np.asarray(right, dtype=float)
    return (a @ b).tolist()


def transpose_matrix(matrix: list[list[float]]) -> list[list[float]]:
    return np.asarray(matrix).T.tolist()


def solve_system(
    matrix: list[list[float]], vector: list[float]
) -> list[float]:
    A = np.asarray(matrix, dtype=float)
    b = np.asarray(vector, dtype=float)
    x = np.linalg.solve(A, b)
    return np.round(x, 6).tolist()


def tensor_channel_mean(tensor: list) -> list:
    t = np.asarray(tensor, dtype=float)
    return np.mean(t, axis=-1).tolist()


def point_distance(first: list[float], second: list[float]) -> float:
    a = np.asarray(first, dtype=float)
    b = np.asarray(second, dtype=float)
    return round(float(np.linalg.norm(a - b)), 6)

