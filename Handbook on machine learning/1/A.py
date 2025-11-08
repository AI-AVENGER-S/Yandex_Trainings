import numpy as np

def construct_matrix(x, y):
    result = np.vstack([x, y])
    return result.T


x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
print(construct_matrix(x, y))