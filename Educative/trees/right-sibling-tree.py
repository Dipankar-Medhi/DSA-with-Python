def rightSiblingTree(root):
    mutate(root, None, None)
    return root


def mutate(node, parent, isLeftChild):
    if node is None:
        return

    mutate(node.left, node, True)
    if parent is None:
        node.right = None
    elif isLeftChild:
        node.right = parent.right
    else:
        if parent.right is None:
            node.right = None
        else:
            node.right = parent.right.left
    mutate(node.right, node, False)
