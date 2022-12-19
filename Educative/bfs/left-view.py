from collections import deque


class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left, self.right = None, None


def leftView(root):
    result = []

    if root is None:
        return result

    queue = deque()
    queue.append(root)

    while queue:
        levelSize = len(queue)

        for i in range(levelSize):
            curr_node = queue.popleft()
            if i == 0:
                result.append(curr_node.val)

            # add children
            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)

    return result


root = TreeNode(1)
root.left = TreeNode(7)
root.right = TreeNode(9)
root.right.left = TreeNode(2)
root.right.right = TreeNode(9)

print(leftView(root))
