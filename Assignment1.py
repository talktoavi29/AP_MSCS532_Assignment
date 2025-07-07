def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

num_list = [10, 3, 7, 2, 8]
sorted_list = insertion_sort(num_list)
print("Sorted in decreasing order:", sorted_list)
