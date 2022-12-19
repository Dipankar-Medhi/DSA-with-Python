
class TreeNode:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left, self.right = left, right


def findSumOfPathNumbers(root):
    return findRootToLeafPathNumbers(root, 0)


def findRootToLeafPathNumbers(currNode, pathSum):
    if currNode is None:
        return 0

    # cal path number of curr node
    pathSum = 10 * pathSum + currNode.val

    # return pathsum if its a leaf node
    if currNode.left is None and currNode.right is None:
        return pathSum

    # traverse left and right subtree
    return findRootToLeafPathNumbers(currNode.left, pathSum) + findRootToLeafPathNumbers(currNode.right, pathSum)


root = TreeNode(1)
root.left = TreeNode(7)
root.right = TreeNode(9)
root.right.left = TreeNode(2)
root.right.right = TreeNode(9)

print(findSumOfPathNumbers(root))
