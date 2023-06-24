from collections import deque
import math


class TreeNode:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left, self.right = left, right


def bottom_view(root):
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

        views[coordinate] = node.val

        if node.left:
            queue.append((node.left, coordinate - 1))
        if node.right:
            queue.append((node.right, coordinate + 1))

    for i in range(start, end + 1):
        if i in views:
            result.append(views[i])

    return result


root = TreeNode(1)
root.left = TreeNode(7)
root.left.left = TreeNode(4)
root.right = TreeNode(9)
root.right.left = TreeNode(2)
root.right.right = TreeNode(9)

print(bottom_view(root))
