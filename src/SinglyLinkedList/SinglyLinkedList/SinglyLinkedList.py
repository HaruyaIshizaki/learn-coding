class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

    def addNextNode(self, newNode):
        tmpNode = self.next
        self.next = newNode
        newNode.next = tmpNode

class SinglyLinkedList:
    def __init__(self, arr) -> None:
        self.head = Node(arr[0])
        self.len = len(arr)

        # 配列->片方向リストの生成
        currentNode = self.head
        for i in range(1, self.len):
            currentNode.next = Node(arr[i])
            currentNode = currentNode.next

        # 末端はNone
        currentNode.next = None

    def searchNodeFromIndex(self, index):
        iterator = self.head
        if index > 0:
            for i in range(index): iterator = iterator.next
        return iterator

    def searchIndex(self, nodeData):
        iterator = self.head
        for index in range(self.len):
            if iterator.data == nodeData: return index
            iterator = iterator.next

    def preappend(self, newNode):
        newNode.next = self.head
        self.head = newNode

    def popFront(self):
        self.head = self.head.next

    def delete(self, index):
        pass

    def printList(self):
        iterator = self.head
        while iterator is not None:
            print(iterator.data, end=" ")
            iterator = iterator.next
        print()

numList = SinglyLinkedList([1,3,45,8,2,77])
numList.printList()
print(numList.searchIndex(77))
print(numList.searchNodeFromIndex(4).data)
numList.head.next.addNextNode(Node(222))
numList.printList()