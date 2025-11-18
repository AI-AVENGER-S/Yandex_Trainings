import numpy as np

def most_frequent(nums):
    unique, counts = np.unique(nums, return_counts=True)
    return unique[np.argmax(counts)]