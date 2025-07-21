import time
import sys
import random
import numpy as np
from randomized_quicksort import randomized_quicksort

sys.setrecursionlimit(5000)

def deterministic_quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less = [x for x in arr[1:] if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr[1:] if x > pivot]
    return deterministic_quicksort(less) + equal + deterministic_quicksort(greater)


def time_sort(func, arr):
    start = time.time()
    func(arr.copy())
    return time.time() - start

sizes = [100, 1000]
input_types = {
    "Random": lambda n: np.random.randint(0, n, size=n).tolist(),
    "Sorted": lambda n: list(range(n)),
    "Reverse": lambda n: list(range(n, 0, -1)),
    "Repeated": lambda n: [5] * n
}

for size in sizes:
    print(f"\nArray Size: {size}")
    for label, generator in input_types.items():
        arr = generator(size)
        rt = time_sort(randomized_quicksort, arr)
        dt = time_sort(deterministic_quicksort, arr)
        print
