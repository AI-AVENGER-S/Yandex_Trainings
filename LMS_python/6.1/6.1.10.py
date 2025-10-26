import numpy as np


def stairs(vector):
    n = len(vector)
    return np.array([vector[(np.arange(n) - i) % n] for i in range(n)])
