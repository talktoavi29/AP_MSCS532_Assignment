import random

def deterministic_select(arr, k):
    if len(arr) <= 5:
        return sorted(arr)[k - 1]

    def chunks(lst, n):
        for i in range(0, len(lst), n):
            yield lst[i:i + n]

    medians = [sorted(chunk)[len(chunk) // 2] for chunk in chunks(arr, 5)]
    pivot = deterministic_select(medians, len(medians) // 2 + 1)

    lows = [el for el in arr if el < pivot]
    highs = [el for el in arr if el > pivot]
    pivots = [el for el in arr if el == pivot]

    if k <= len(lows):
        return deterministic_select(lows, k)
    elif k <= len(lows) + len(pivots):
        return pivot
    else:
        return deterministic_select(highs, k - len(lows) - len(pivots))


def randomized_select(arr, k):
    if len(arr) == 1:
        return arr[0]

    pivot = random.choice(arr)
    lows = [el for el in arr if el < pivot]
    highs = [el for el in arr if el > pivot]
    pivots = [el for el in arr if el == pivot]

    if k <= len(lows):
        return randomized_select(lows, k)
    elif k <= len(lows) + len(pivots):
        return pivot
    else:
        return randomized_select(highs, k - len(lows) - len(pivots))


if __name__ == "__main__":
    ratings = [3, 5, 2, 4, 5, 1, 3]
    k = 3
    print(f"{k}rd smallest rating (deterministic):", deterministic_select(ratings, k))
    print(f"{k}rd smallest rating (randomized):", randomized_select(ratings, k))
