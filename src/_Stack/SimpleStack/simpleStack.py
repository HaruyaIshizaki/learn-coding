class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class Stack:
    def __init__(self) -> None:
        self.head = None

    def pop(self):
        if self.head is None: return None
        popTarget = self.head
        self.head = self.head.next
        return popTarget

    def push(self, data):
        tmpNode = self.head
        self.head = Node(data)
        self.head.next = tmpNode

    def peek(self):
        if self.head is None: return None
        return self.head.data