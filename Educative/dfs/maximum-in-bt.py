import math


class TreeNode:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left, self.right = left, right


def max_in_binarytree(root):
    if root is None:
        return -math.inf

    result = root.val
    leftMax = max_in_binarytree(root.left)
    rightMax = max_in_binarytree(root.right)

    if leftMax > result:
        result = leftMax
    if rightMax > result:
        result = rightMax

    return result


root = TreeNode(1)
root.left = TreeNode(7)
root.right = TreeNode(9)
root.right.left = TreeNode(2)
root.right.right = TreeNode(9)

print(max_in_binarytree(root))
