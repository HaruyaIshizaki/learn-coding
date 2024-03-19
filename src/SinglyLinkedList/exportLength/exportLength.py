# 片方向リストの長さを返す

class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self, arr):
        self.head = SinglyLinkedListNode(arr[0])
        self.len = len(arr)

        currentNode = self.head
        for i in range(1,self.len):
            currentNode.next = SinglyLinkedListNode(arr[i])
            currentNode = currentNode.next
        currentNode.next = None

    def exportLength(self):
        print('debug')
        return self.len

numList = SinglyLinkedList([3,2,1,5,6,4])
print(numList.exportLength())