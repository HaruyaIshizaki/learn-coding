class BinaryTree:
    def __init__(self, data) -> None:
        self.data = data
        # ノードの左の子
        self.left = None
        # ノードの右の子
        self.right = None

binaryTree = BinaryTree(1)
node2 = BinaryTree(2)
node3 = BinaryTree(3)

binaryTree.left = node2
binaryTree.right = node3

print('Root: ' + str(binaryTree.data))
print('Left: ' + str(binaryTree.left.data))
print('Right: ' + str(binaryTree.right.data))