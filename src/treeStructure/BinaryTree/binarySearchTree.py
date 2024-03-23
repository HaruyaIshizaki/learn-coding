import math

class BinaryTree:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self, arrList):
        sortedList = sorted(arrList)
        self.root = BinarySearchTree.sortedArrayBST(sortedList)

    @staticmethod
    def sortedArrayBST(array):
        if len(array) == 0: return None
        return BinarySearchTree.sortedArrayBTSHelper(array, 0, len(array)-1)

    @staticmethod
    def sortedArrayBTSHelper(arr, start, end):
        # 葉ノード生成
        if start == end: return BinaryTree(arr[start], None, None)

        # ノードが2つ以上あるため、二分木を再帰的に作る処理
        mid = math.floor((start + end)/2)
        left = None
        if mid-1 >= start:
            left = BinarySearchTree.sortedArrayBTSHelper(arr, start, mid-1)
        right = None
        if end >= mid+1:
            right = BinarySearchTree.sortedArrayBTSHelper(arr, mid+1, end)

        # 根ノード生成
        root = BinaryTree(arr[mid], left, right)
        return root

    def keyExist(self, key):
        iterator = self.root
        while iterator is not None:
            if iterator.data == key:return True
            if iterator.data > key: iterator = iterator.left
            else: iterator = iterator.right

        return False

    def search(self, key):
        iterator = self.root
        while iterator is not None:
            if iterator.data == key: return iterator
            if iterator.data > key: iterator = iterator.left
            else: iterator = iterator.right

        return None

balancedBST = BinarySearchTree([1,2,3,4,5,6,7,8,9,10,11])
print(balancedBST.keyExist(6))
print(balancedBST.search(6).data)
print(balancedBST.keyExist(2))
print(balancedBST.search(2).data)
print(balancedBST.search(34))