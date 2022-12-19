class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.neighbors = []


def clone_recursive(root, nodes_completed):
    if root is None:
        return None

    node = Node(root.data)
    nodes_completed[root] = node

    for n in root.neighbors:
        x = nodes_completed.get(n)
        # add to stack is neighbors not in hashmap
        if x is None:
            node.neighbors += [clone_recursive(n, nodes_completed)]
        else:
            node.neighbors += [x]

    return node


def clone(root):
    nodes_completed = {}
    return clone_recursive(root, nodes_completed)
