import numpy as np


def update_border(array, size, value):
    new_array = np.copy(array)
    reshaped = new_array.reshape(size)
    reshaped[0, :] += value
    reshaped[-1, :] += value
    reshaped[1:-1, 0] += value
    reshaped[1:-1, -1] += value
    return new_array


array = np.arange(1, 16)
new_array = update_border(array, (5, 3), 5)
print(new_array)
