from data_structures.bst import BSTNode
from data_structures.trie import Trie
from data_structures.hash_map import HashMap

# Example Usage
bst = BSTNode(4.5, {"name": "Raj Electrician"})
bst.insert(4.8, {"name": "Ali Plumber"})
bst.insert(4.2, {"name": "Simran Tailor"})

trie = Trie()
for service in ["plumber", "plumbing", "tailor", "carpenter"]:
    trie.insert(service)

hash_map = HashMap()
hash_map.insert("plumber", [101, 102])
