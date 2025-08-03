class HashMap:
    def __init__(self, size=1009):  # Prime number for better distribution
        self.size = size
        self.map = [[] for _ in range(self.size)]

    def _hash(self, key):
        return sum(ord(c) for c in key) % self.size

    def set(self, key, value):
        index = self._hash(key)
        for i, (k, _) in enumerate(self.map[index]):
            if k == key:
                self.map[index][i] = (key, value)
                return
        self.map[index].append((key, value))

    def get(self, key):
        index = self._hash(key)
        for k, v in self.map[index]:
            if k == key:
                return v
        return None

    def remove(self, key):
        index = self._hash(key)
        self.map[index] = [(k, v) for (k, v) in self.map[index] if k != key]
