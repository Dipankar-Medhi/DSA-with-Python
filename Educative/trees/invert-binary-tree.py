from collections import deque


class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None


# O(n) time | O(n) space
def invertBinaryTree(root):
    queue = deque()
    queue.append(root)
    res = []
    while queue:
        curr = queue.popleft()
        # swap the children nodes before adding them to the queue
        swapLeftandRight(curr)
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)

        res.append(curr.val)

    return res


def swapLeftandRight(node):
    node.left, node.right = node.right, node.left


## Recursive
# O(n) time  | O(d) depth of recursive stack
def invert_binary_tree(root):
    if root is None:
        return
    swapLeftandRight(root)
    invert_binary_tree(root.left)
    invert_binary_tree(root.right)


root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
print(invertBinaryTree(root))
