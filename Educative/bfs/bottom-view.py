from collections import deque
import math


class TreeNode:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left, self.right = left, right


def bottom_view(root):
    """
    Given the root of a binary tree, this function returns the bottom view of the tree as a list.
    The bottom view of a tree is defined as the nodes that would be visible if you looked at the tree
    from the bottom up, where each node is represented by its value.

    Args:
    - root: the root of the binary tree

    Returns:
    - A list of the values of the nodes that make up the bottom view of the tree. The order of the
    values in the list corresponds to the left-to-right order of the nodes in the bottom view.
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

        views[coordinate] = node.val

        if node.left:
            queue.append((node.left, coordinate - 1))
        if node.right:
            queue.append((node.right, coordinate + 1))
    print("views:", views)
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
