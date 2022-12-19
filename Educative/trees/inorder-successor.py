def find_min(root):
    if root is None:
        return None

    while root.left:
        root = root.left

    return root


def inorder_successor_bst(root, d):
    if root == None:
        return None

    successor = None

    while root:
        if root.data < d:
            root = root.right
        elif root.data > d:
            successor = root
            root = root.left
        else:  # if root.data == d, then succcessor willl be either min of right subtree or the prev successor
            if root.right:
                successor = find_min(root.right)
            break
    return successor


# time O(logn) | space O(1)
