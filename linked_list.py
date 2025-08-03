class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_front(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_end(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def delete(self, value):
        curr = self.head
        prev = None
        while curr:
            if curr.value == value:
                if prev:
                    prev.next = curr.next
                else:
                    self.head = curr.next
                return True
            prev = curr
            curr = curr.next
        return False

    def traverse(self):
        curr = self.head
        while curr:
            print(curr.value, end=" -> ")
            curr = curr.next
        print("None")


if __name__ == "__main__":
    print("=== Linked List Demo ===")
    ll = SinglyLinkedList()
    ll.insert_end("plumber")
    ll.insert_end("electrician")
    ll.insert_front("tailor")
    ll.traverse()

    print("Deleting 'electrician'...")
    ll.delete("electrician")
    ll.traverse()
