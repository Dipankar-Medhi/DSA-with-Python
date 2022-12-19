import sys


def is_valid_bst(root, min, max):
    if root is None:
        return True

    if root.data < min or root.data > max:
        return False

    return is_valid_bst(root.left, min, root.data - 1) and is_valid_bst(
        root.right, root.data + 1, max
    )


def is_bst(root):
    return is_valid_bst(root, -sys.maxsize - 1, sys.maxsize)


# -----#
prev = -1


def isValidBST(root):
    return is_BST(root)


def is_BST(root):
    global prev

    if root is None:
        return True

    if is_BST(root.left) is False:
        return False

    if prev > root.data and prev != -1:
        return False

    prev = root.data

    if is_BST(root.right) is False:
        return False

    return True
