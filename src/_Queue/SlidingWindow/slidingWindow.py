class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None

    def peekFront(self):
        if self.head is None: return None
        return self.head.data

    def peekBack(self):
        if self.tail is None: return None
        return self.tail.data

    def enqueueFront(self,data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.head.prev = Node(data)
            self.head.prev.next = self.head
            self.head = self.head.prev

    def enqueueBack(self,data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next = Node(data)
            self.tail.next.prev = self.tail
            self.tail = self.tail.next

    def dequeueFront(self):
        if self.head is None: return None

        temp = self.head
        self.head = self.head.next
        if self.head is None: self.tail = None
        else: self.head.prev = None

        return temp.data

    def dequeueBack(self):
        if self.tail is None: return None

        temp = self.tail
        self.tail = self.tail.prev

        if self.tail is None: self.head = None
        else: self.tail.next = None
        return temp.data

def getMaxWindows(arr, k):
    result = []
    deque = Deque()
    for i in arr[:k]:
        deque.enqueueFront(i)

    for data in arr[k:]:
        print(deque.peekBack())
        print(deque.peekFront())

        # スライドウィンドウを一つ進める
        deque.dequeueBack()
        deque.enqueueFront(data)

    return result

print(getMaxWindows([34,35,64,34,10,2,14,5,353,23,35,63,23], 4)); #[64, 64, 64, 34, 14, 353, 353, 353, 353, 63]
