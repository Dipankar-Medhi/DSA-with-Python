"""
Given a binary tree of integers root, create a function that reverses it left to right in-place.
"""

# Using Recursion ---> Time O(n) space O(h)


def reverseTree(tree):
    # when there is no children
    if tree is None:
        return
    # swap the childrens
    tree.left, tree.right = tree.right, tree.left
    # doing the same for the children's children
    reverseTree(tree.left)
    reverseTree(tree.right)
