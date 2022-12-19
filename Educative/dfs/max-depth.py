class TreeNode:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left, self.right = left, right


def maxDepth(root):
    if root is None:
        return 0
    depth = solve(root, 1)
    return depth


def solve(currNode, depth):
    if currNode is None:
        return depth

    if currNode.left is None and currNode.right is None:
        return depth

    lefttreedepth = solve(currNode.left, depth + 1)
    righttreedepth = solve(currNode.right, depth + 1)

    depth = max(lefttreedepth, righttreedepth)

    return depth


root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)

print(maxDepth(root))
