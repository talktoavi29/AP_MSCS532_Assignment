class BSTNode:
    def __init__(self, rating, provider_data):
        self.rating = rating
        self.data = provider_data
        self.left = None
        self.right = None

    def insert(self, rating, provider_data):
        if rating < self.rating:
            self.left = self.left.insert(rating, provider_data) if self.left else BSTNode(rating, provider_data)
        else:
            self.right = self.right.insert(rating, provider_data) if self.right else BSTNode(rating, provider_data)
        return self

    def inorder(self, results=None):
        if results is None:
            results = []
        if self.left:
            self.left.inorder(results)
        results.append((self.rating, self.data))
        if self.right:
            self.right.inorder(results)
        return results
