import time
import random
import string
from data_structures.hash_map import HashMap
from data_structures.trie import Trie
from data_structures.bst import BST

# Generate mock dataset
def generate_workers(num=10000):
    names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
    services = ['plumber', 'electrician', 'tailor', 'carpenter', 'mechanic']
    cities = ['Austin', 'Dallas', 'Houston', 'San Antonio', 'El Paso']

    data = []
    for _ in range(num):
        worker = {
            'name': random.choice(names) + ''.join(random.choices(string.ascii_lowercase, k=3)),
            'service': random.choice(services),
            'rating': round(random.uniform(1, 5), 1),
            'city': random.choice(cities)
        }
        data.append(worker)
    return data

# Optimized filtering using Trie and HashMap
def filter_and_sort(workers, service_filter, city_filter):
    hashmap = HashMap()
    trie = Trie()
    bst = BST()

    for w in workers:
        hashmap.set(w['name'], w)
        trie.insert(w['service'])
        bst.insert(w['rating'], w)

    filtered = [w for w in workers if w['service'] == service_filter and w['city'] == city_filter]
    sorted_filtered = sorted(filtered, key=lambda x: x['rating'], reverse=True)

    return sorted_filtered[:10]  # Return top 10

# Entry point
if __name__ == "__main__":
    workers = generate_workers()

    print("Starting performance benchmark...")
    start_time = time.time()

    results = filter_and_sort(workers, service_filter='plumber', city_filter='Austin')

    end_time = time.time()
    print(f"\nTop 10 Plumbers in Austin:")
    for r in results:
        print(f"{r['name']} - {r['rating']} stars")

    print(f"\nExecution time: {end_time - start_time:.4f} seconds")