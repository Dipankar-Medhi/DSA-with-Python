from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def levelOrderTraverse(root):
    result = []
    if root is None:
        return result

    q = deque()
    q.append(root)

    while q:
        level = len(q)
        currentLevel = []

        for _ in range(level):

            node = q.popleft()
            currentLevel.append(node.val)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        result.append(currentLevel)
    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    print("Level Order Traversal: {}".format(str(levelOrderTraverse(root))))


main()
