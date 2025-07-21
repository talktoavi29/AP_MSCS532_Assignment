import time
import random
import numpy as np
from heapsort import heapsort
from randomized_quicksort import randomized_quicksort

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

def time_sort(func, arr):
    start = time.time()
    func(arr.copy())
    return time.time() - start

sizes = [100, 1000, 5000]
types = {
    "Random": lambda n: np.random.randint(0, n, n).tolist(),
    "Sorted": lambda n: list(range(n)),
    "Reverse": lambda n: list(range(n, 0, -1))
}

for size in sizes:
    print(f"\nArray Size: {size}")
    for label, gen in types.items():
        arr = gen(size)
        ht = time_sort(heapsort, arr)
        qt = time_sort(randomized_quicksort, arr)
        mt = time_sort(merge_sort, arr)
        print(f"{label:<10} | Heap: {ht:.5f}s | Quick: {qt:.5f}s | Merge: {mt:.5f}s")
