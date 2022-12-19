class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSymmetric(root):
    if root is None:
        return True

    return solve(root.left, root.right)


def solve(leftNode, rightNode):

    if leftNode and rightNode:
        if leftNode.val != rightNode.val:
            return False

    if leftNode is None or rightNode is None:
        return leftNode == rightNode

    return solve(leftNode.left, rightNode.right) and solve(leftNode.right, rightNode.left)


root = TreeNode(1)
root.left = TreeNode(7)
root.right = TreeNode(7)
root.left.left = TreeNode(9)
root.left.right = TreeNode(2)
root.right.left = TreeNode(2)
root.right.right = TreeNode(9)

print(isSymmetric(root))
