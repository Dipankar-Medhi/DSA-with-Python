from collections import deque
import math


class TreeNode:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left, self.right = left, right


def top_view(root):
    """
    Given the root of a binary tree, returns a list of the nodes visible from the top view of the tree from left to right.

    :param root: The root node of the binary tree.
    :type root: TreeNode
    :return: A list of the nodes visible from the top of the tree.
    :rtype: List[int]
    """
    result = []
    views = {}
    queue = deque()
    queue.append((root, 0))
    start = math.inf
    end = -math.inf
    while queue:

        node, coordinate = queue.popleft()

        start = min(start, coordinate)
        end = max(end, coordinate)

        if coordinate not in views:
            views[coordinate] = node.val

        if node.left:
            queue.append((node.left, coordinate - 1))
        if node.right:
            queue.append((node.right, coordinate + 1))

    for i in range(start, end + 1):
        if i in views:
            result.append(views[i])

    return result


node = TreeNode(1)
node.left = TreeNode(2)
node.right = TreeNode(3)
node.left.left = TreeNode(4)
node.left.right = TreeNode(5)
node.right.left = TreeNode(6)
node.right.right = TreeNode(7)

print(top_view(node))
