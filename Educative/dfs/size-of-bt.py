class TreeNode:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left, self.right = left, right


def size_of_binary_tree(root):
    if root is None:
        return 0
    result = recurse(root, 0)
    return result


def recurse(node, size):
    if node is None:
        return size

    if node.left is None and node.right is None:
        return size

    leftSize = recurse(node.left, size + 1)
    rightSize = recurse(node.right, size + 1)

    return leftSize + rightSize


root = TreeNode(1)
root.left = TreeNode(7)
root.right = TreeNode(9)
root.right.left = TreeNode(2)
root.right.right = TreeNode(9)

print("size of binary Tree is:", size_of_binary_tree(root))
