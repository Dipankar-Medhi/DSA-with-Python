"""
Two trees ‘A’ and ‘B’ are identical if:

data on their roots is the same or both roots are null left sub-tree of ‘A’ is identical to the left sub-tree of 'B’ right sub-tree of ‘A’ is identical to the right sub-tree of 'B’ To solve this problem, we’ll do a depth-first traversal on both trees simultaneously and keep comparing the data at each level.
"""


def are_identical(root1, root2):
    if root1 == None and root2 == None:
        return True

    if root1 != None and root2 != None:
        return (
            root1.val == root2.val
            and are_identical(root1.left, root2.left)
            and are_identical(root1.right, root2.right)
        )
    return False
