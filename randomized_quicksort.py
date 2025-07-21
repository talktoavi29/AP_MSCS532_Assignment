import random

def randomized_quicksort(arr):
    def quicksort(arr, low, high):
        if low < high:
            pivot_index = random_partition(arr, low, high)
            quicksort(arr, low, pivot_index - 1)
            quicksort(arr, pivot_index + 1, high)

    def random_partition(arr, low, high):
        rand_pivot = random.randint(low, high)
        arr[high], arr[rand_pivot] = arr[rand_pivot], arr[high]
        return partition(arr, low, high)

    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    quicksort(arr, 0, len(arr) - 1)
    return arr

test_cases = [
    [],
    [1],
    [3, 1, 4, 1, 5, 9, 2],
    [5, 5, 5, 5],
    list(range(10)),
    list(range(10, 0, -1))
]

for test in test_cases:
    print(f"Original: {test} => Sorted: {randomized_quicksort(test.copy())}")