import random

class Contractor:
    def __init__(self, name, rating, distance_km, idle_minutes):
        self.name = name
        self.rating = rating
        self.distance_km = distance_km
        self.idle_minutes = idle_minutes

    def priority_score(self):
        return (5 - self.rating) * 10 + self.distance_km + self.idle_minutes / 5

    def __repr__(self):
        return f"{self.name} (Score: {self.priority_score():.2f})"

def quicksort_contractors(contractors):
    if len(contractors) <= 1:
        return contractors
    pivot = contractors[-1]
    left = [c for c in contractors[:-1] if c.priority_score() <= pivot.priority_score()]
    right = [c for c in contractors[:-1] if c.priority_score() > pivot.priority_score()]
    return quicksort_contractors(left) + [pivot] + quicksort_contractors(right)

contractors = [
    Contractor("Raj Tailor", 4.7, 1.2, 30),
    Contractor("Ali Electrician", 4.3, 0.5, 10),
    Contractor("Simran Stitching", 5.0, 3.0, 90),
    Contractor("Kumar Plumber", 4.1, 0.3, 15),
    Contractor("Fatima Handywoman", 4.9, 2.5, 50)
]

sorted_contractors = quicksort_contractors(contractors)
print("Ranked Contractors:")
for c in sorted_contractors:
    print(c)
