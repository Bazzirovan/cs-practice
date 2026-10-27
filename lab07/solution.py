import numpy as np

def reshape_rows(values: list[float], width: int) -> list[list[float]]:
    if len(values) == 0 or len(values) % width != 0: return []
    arr = np.asarray(values)
    return arr.reshape(-1, width).tolist()


def block(matrix: list[list[float]], rows: list[int], columns: list[int]) -> list[list[float]]:
    arr = np.asarray(matrix)
    return arr[np.ix_(rows, columns)].tolist()



