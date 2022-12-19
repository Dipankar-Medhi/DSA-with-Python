class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def findPath(root, sequence):
    if root is None:
        return len(sequence) == 0

    return findPathRecursion2(root, sequence, 0)


def findPathRecursion(currNode, sequence, seqIdx):
    if currNode is None:
        return False

    seqLen = len(sequence)

    # False if sequence index is out of bound
    # or the val of node doesnot match
    if seqIdx >= seqLen or currNode.val != sequence[seqIdx]:
        return False

    # true if the node is leaf i.e we have reached the end and found the path
    if currNode.left is None and currNode.right is None and seqIdx == seqLen - 1:
        return True

    # recursively call to traverse left and right subtree
    # True if any of the two return True
    return findPathRecursion(currNode.left, sequence, seqIdx + 1) or findPathRecursion(
        currNode.right, sequence, seqIdx + 1
    )


def findPathRecursion2(node, sequence, idx):
    if node is None:
        return False
    n = len(sequence)

    if idx >= n or node.val != sequence[idx]:
        return False
    if node.left is None and node.right is None and idx == n - 1:
        return True

    if findPathRecursion2(node.left, sequence, idx + 1):
        return True
    elif findPathRecursion2(node.right, sequence, idx + 1):
        return True
    else:
        return False


root = TreeNode(1)
root.left = TreeNode(7)
root.right = TreeNode(9)
root.right.left = TreeNode(2)
root.right.right = TreeNode(9)

print(findPath(root, [1, 9, 2]))
