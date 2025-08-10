# main.py
import random, time
from typing import Dict, List
from data_structures.avl import AVLTree
from data_structures.trie import CompressedTrie
from data_structures.hash_map import OpenAddressMap

class RecommendationEngine:
    """
    Glue layer: Trie (services) -> Hash map (service->provider IDs) -> AVL (rating ranking)
    """
    def __init__(self) -> None:
        self.trie = CompressedTrie()
        self.service_to_providers = OpenAddressMap(2048)
        self.providers_by_rating = AVLTree()

    def add_provider(self, provider: Dict) -> None:
        # provider: {id, name, city, rating, services: [str]}
        # index by rating in AVL
        # If two providers share identical rating, add a tiny epsilon to keep keys unique
        key = provider["rating"]
        while self.providers_by_rating.get(key) is not None:
            key = float(f"{key:.3f}") + 1e-6
        self.providers_by_rating.insert(key, provider)

        # index each service in trie and map service->ids
        for svc in provider["services"]:
            self.trie.insert(svc.lower(), score=provider["rating"])
            lst: List[int] = self.service_to_providers.get(svc.lower(), [])
            if lst is None:
                lst = []
            lst.append(provider["id"])
            self.service_to_providers.put(svc.lower(), lst)

    def search(self, prefix: str, k: int = 10) -> List[Dict]:
        suggestions = [term for term, _ in self.trie.suggest(prefix.lower(), k=5)]
        candidate_ids: List[int] = []
        for term in suggestions:
            ids = self.service_to_providers.get(term, [])
            if ids:
                candidate_ids.extend(ids)

        # dedupe
        seen = set()
        candidate_ids = [x for x in candidate_ids if not (x in seen or seen.add(x))]

        # scan AVL in descending rating and filter by id
        wanted = set(candidate_ids)
        results: List[Dict] = []
        for _, prov in self.providers_by_rating.inorder(reverse=True):
            if prov["id"] in wanted:
                results.append(prov)
                if len(results) == k:
                    break
        return results

def _fake_name() -> str:
    first = random.choice(["Ali","Raj","Mina","Sara","Luis","Ana","Ravi","Kim","Noah","Leah"])
    last  = random.choice(["Plumber","Electric","Handy","Tailor","Fixit","Pro","Ace","Works"])
    return f"{first} {last}"

def _fake_services() -> List[str]:
    bank = [
        "plumber", "plumbing repair", "electrician", "circuit repair", "tailor",
        "seamstress", "hvac", "ac repair", "carpenter", "roof repair", "gardener",
        "pest control", "window cleaning", "house cleaning"
    ]
    n = random.randint(1, 3)
    return random.sample(bank, n)

def build_demo_dataset(n: int = 10000) -> RecommendationEngine:
    random.seed(7)
    eng = RecommendationEngine()
    for i in range(n):
        prov = {
            "id": 1000 + i,
            "name": _fake_name(),
            "city": random.choice(["Austin","Dallas","Houston","San Antonio"]),
            "rating": round(random.uniform(3.5, 5.0), 2),
            "services": _fake_services(),
        }
        eng.add_provider(prov)
    return eng

if __name__ == "__main__":
    start_time = time.time()
    engine = build_demo_dataset(10000)
    build_done = time.time()

    q = "plu"
    results = engine.search(q, k=10)
    end_time = time.time()

    print(f"Dataset built in: {build_done - start_time:.3f}s")
    print(f"\nTop results for prefix '{q}':")
    for r in results:
        print(f"  {r['name']}  —  {r['rating']}★  ({', '.join(r['services'])})")

    print(f"\nExecution time (query only): {end_time - build_done:.4f} seconds")