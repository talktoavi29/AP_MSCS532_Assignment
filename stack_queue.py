class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def display(self):
        print("Stack:", self.stack)


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self.queue.pop(0)

    def front(self):
        if self.is_empty():
            return None
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def display(self):
        print("Queue:", self.queue)


if __name__ == "__main__":
    # Stack example
    print("=== Stack Demo ===")
    stack = Stack()
    stack.push("plumber")
    stack.push("tailor")
    stack.push("electrician")
    stack.display()
    print("Popped:", stack.pop())
    stack.display()

    # Queue example
    print("\n=== Queue Demo ===")
    queue = Queue()
    queue.enqueue("customer1")
    queue.enqueue("customer2")
    queue.enqueue("customer3")
    queue.display()
    print("Dequeued:", queue.dequeue())
    queue.display()
