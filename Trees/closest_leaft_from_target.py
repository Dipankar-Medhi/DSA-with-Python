"""
Given a binary tree where every node has a unique value, and a target key k, 
find the value of the nearest leaf node to target k in the tree. 
If there is no such node, return -1.

"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


INT_MAX = 2**32


def closest_down(node: TreeNode):
    """Find the closest leaf from the subtree"""
    if node is None:
        return INT_MAX

    if node.left is None and node.right is None:
        return 0

    return min(closest_down(node.left), closest_down(node.right)) + 1


def util_func(root: TreeNode, k: int, ancestors: list, index: int):
    if root is None:
        return INT_MAX

    if root.val == k:
        res = closest_down(root)

        # now check with the other nodes of the parent node
        for i in reversed(range(0, index)):
            closest = closest_down(ancestors[i])
            res = min(res, index - i + closest)

        return res

    ancestors[index] = root

    return min(
        util_func(root.left, k, ancestors, index + 1),
        util_func(root.right, k, ancestors, index + 1),
    )


def find_closest(root, k):
    ancestors = [None for i in range(100)]  # assume 100 ht of tree
    return util_func(root, k, ancestors, 0)


root = TreeNode("A")
root.left = TreeNode("B")
root.right = TreeNode("C")
root.right.left = TreeNode("E")
root.right.right = TreeNode("F")
root.right.left.left = TreeNode("G")
root.right.left.left.left = TreeNode("I")
root.right.left.left.right = TreeNode("J")
root.right.right.right = TreeNode("H")
root.right.right.right.left = TreeNode("K")

print("Distance of the closest leaft from C is:", find_closest(root, "C"))
