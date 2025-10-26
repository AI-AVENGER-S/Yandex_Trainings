import numpy as np


def multiplication_matrix(n) -> np.array:
    matrix = np.arange(1, n + 1)
    return matrix * matrix[:, None]


print(multiplication_matrix(5))
