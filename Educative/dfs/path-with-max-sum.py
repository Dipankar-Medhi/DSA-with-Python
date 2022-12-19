import math


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class MaxPathSum:
    def findMaxPathSum(self, root):
        self.globalMaxSum = -math.inf
        self.findMaxPathSumRecursive(root)
        return self.globalMaxSum

    def findMaxPathSumRecursive(self, currNode):
        if currNode is None:
            return 0

        maxLeftSum = self.findMaxPathSumRecursive(currNode.left)
        maxRightSum = self.findMaxPathSumRecursive(currNode.right)

        # ignore paths with -ve sums
        maxLeftSum = max(maxLeftSum, 0)
        maxRightSum = max(maxRightSum, 0)

        # max path sum at current node will be
        # equal to sum of left + right + current node value
        localMaxSum = maxLeftSum + maxRightSum + currNode.val

        self.globalMaxSum = max(self.globalMaxSum, localMaxSum)

        # max sum of any path will be equal to
        # sum of max left tree or right + curr val
        return max(maxLeftSum, maxRightSum) + currNode.val


def main():
    maxPathSum = MaxPathSum()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)

    print(maxPathSum.findMaxPathSum(root))


main()
