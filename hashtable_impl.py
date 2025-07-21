class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value  
                return
        self.table[index].append([key, value]) 

    def search(self, key):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None

    def delete(self, key):
        index = self.hash_function(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return True
        return False

if __name__ == "__main__":
    ht = HashTable()

#Insert
    ht.insert("A101", "Abhishek Pandey")
    ht.insert("A102", "Asmi Pokharel")
    ht.insert("A103", "Pramesh Bhandari")
    ht.insert("A102", "Aaradhya Pandey") 

#Search
    print("Search A102:", ht.search("A102")) 
    print("Search A104:", ht.search("A104")) 

#Delete
    print("Delete A101:", ht.delete("A101")) 
    print("Search A101:", ht.search("A101")) 

