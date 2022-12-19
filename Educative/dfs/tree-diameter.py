"""
longest path between any two leaf nodes. The diameter of a tree may or may not pass through the root.
"""


class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left, self.right = None, None


class TreeDiameter:
    def __init__(self) -> None:
        self.treeDiameter = 0

    def findDiameter(self, root):
        self.calHeight(root)
        return self.treeDiameter

    def calHeight(self, currNode):
        if currNode is None:
            return 0

        leftTreeHeight = self.calHeight(currNode.left)
        rightTreeHeight = self.calHeight(currNode.right)

        # diameter of current node is equal to
        # the height of left subtree +
        # height of right subtree + 1
        diameter = leftTreeHeight + rightTreeHeight + 1

        # update the global tree diameter
        self.treeDiameter = max(self.treeDiameter, diameter)

        # height of current node will be equal to the max of
        # height of left or right subtree + 1
        return max(leftTreeHeight, rightTreeHeight) + 1


def main():
    treeDiameter = TreeDiameter()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    root.right.right.left = TreeNode(7)
    root.right.left.right = TreeNode(8)

    print("Tree Diameter: ", treeDiameter.findDiameter(root))


if __name__ == "__main__":
    main()
