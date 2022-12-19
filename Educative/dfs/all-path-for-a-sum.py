"""
- Store every path from root to left that equals to the sum.
"""


class TreeNode:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left, self.right = left, right


def findPath(root, sum):
    allPaths = []
    findPathrecursion(root, sum, [], allPaths)
    return allPaths


def findPathrecursion(currNode, sum, currPath, allPaths):
    if currNode is None:
        return

    # add currNode to path
    currPath.append(currNode.val)

    # if currNOde is leaf and equal to sum, save
    if currNode.val == sum and currNode.left is None and currNode.right is None:
        allPaths.append(list(currPath))
    else:
        # traverse the left sub-tree
        findPathrecursion(currNode.left, sum - currNode.val, currPath, allPaths)
        # traverse right sub-tree
        findPathrecursion(currNode.right, sum - currNode.val, currPath, allPaths)

    # remove the current node from path to backtrack while going up the call stack
    del currPath[-1]


root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)

print(findPath(root, 28))

# Time O(n2)
# Space O(nlogn)
