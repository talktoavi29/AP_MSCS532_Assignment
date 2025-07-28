import random 
import randomized_qs as qs
def generate_random_contractors(n):
    return [
        qs.Contractor(
            f"Worker{i}",
            random.uniform(3.5, 5.0),
            random.uniform(0.1, 5.0),
            random.randint(0, 240)
        ) for i in range(n)
    ]

import time

def time_sort(func, data):
    start = time.time()
    func(data.copy())
    return time.time() - start

contractor_list = generate_random_contractors(10000)
print("Deterministic Quicksort:", time_sort(qs.quicksort_contractors, contractor_list))

def randomized_quicksort_contractors(contractors):
    if len(contractors) <= 1:
        return contractors
    pivot = random.choice(contractors)
    rest = [c for c in contractors if c != pivot]
    left = [c for c in rest if c.priority_score() <= pivot.priority_score()]
    right = [c for c in rest if c.priority_score() > pivot.priority_score()]
    return randomized_quicksort_contractors(left) + [pivot] + randomized_quicksort_contractors(right)

print("Randomized Quicksort:", time_sort(randomized_quicksort_contractors, contractor_list))