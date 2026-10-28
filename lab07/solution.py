import numpy as np

def reshape_rows(values: list[float], width: int) -> list[list[float]]:
    if len(values) == 0 or len(values) % width != 0: return []
    arr = np.asarray(values)
    return arr.reshape(-1, width).tolist()


def block(matrix: list[list[float]], rows: list[int], columns: list[int]) -> list[list[float]]:
    arr = np.asarray(matrix)
    return arr[np.ix_(rows, columns)].tolist()


def column_means(matrix: list[list[float]]) -> list[float]:
    if len(matrix) == 0: return []
    arr = np.asarray(matrix)
    res = np.mean(arr, axis = 0)
    res = np.round(res, 6)
    return res.tolist()


def column_range(matrix: list[list[float]], column: int) -> float:
    if len(matrix) == 0: return 0.0
    arr = np.asarray(matrix)
    res = np.ptp(arr[:, column])
    return round(float(res), 6)



if __name__ == "__main__":
    # Здесь могли бы быть ваши тесты =-) 
