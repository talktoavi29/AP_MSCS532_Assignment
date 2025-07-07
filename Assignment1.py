arr = [5, 2, 9, 1, 6]

for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    while j >= 0 and arr[j] < key:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key

print("Sorted in decreasing order:", arr)
