class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None


# O(n) time | O(n) space
## Grab the leftmost node of right subtree and rightmost node of left subtree.
def flattenNodes(root):
    res = []
    inOrderNodes = getInOrderNodes(root, [])

    for i in range(len(inOrderNodes) - 1):
        leftNode = inOrderNodes[i]
        rightNode = inOrderNodes[i + 1]
        leftNode.right = rightNode
        rightNode.left = leftNode
        res.append(inOrderNodes[i].val)
    return res


def getInOrderNodes(tree, arr):
    if tree:
        getInOrderNodes(tree.left, arr)
        arr.append(tree)
        getInOrderNodes(tree.right, arr)

    return arr


## Recursive
def flattenBinaryTree(root):
    flattenTree(root)


def flattenTree(node):
    if node.left is None:
        leftMost = node
    else:
        leftSubtreeleftMost, leftSubtreerightMost = flattenTree(node.left)
        connectNodes(leftSubtreerightMost, node)
        leftMost = leftSubtreeleftMost
    if node.right is None:
        rightMost = node
    else:
        rightSubtreeleftMost, rightSubtreerightMost = flattenTree(node.right)
        connectNodes(node, rightSubtreeleftMost)
        rightMost = rightSubtreerightMost

    return [leftMost, rightMost]


def connectNodes(left, right):
    left.right = right
    right.left = left


root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
print(flattenNodes(root))
