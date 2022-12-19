def print_left_perimeter(root, result):
    if root:
        if root.left:
            # print(root.data)
            result.append(str(root.data))
            print_left_perimeter(root.left, result)

        elif root.right:
            # print (root.data)
            result.append(str(root.data))
            print_left_perimeter(root.right, result)


def print_right_perimeter(root, result):
    if root:
        if root.right:
            print_right_perimeter(root.right, result)
            result.append(str(root.data))
            # print(root.data)

        elif root.left:
            print_right_perimeter(root.left, result)
            result.append(str(root.data))
            # print(root.data)


def print_leaf_nodes(root, result):
    if root:
        print_leaf_nodes(root.left, result)

        # Print this node it is a leaf node
        if root.left is None and root.right is None:
            # print(root.data)
            result.append(str(root.data))

        print_leaf_nodes(root.right, result)


def display_tree_perimeter(root):
    result = []
    if root is not None:
        # print(root.data)
        result.append(str(root.data))

        print_left_perimeter(root.left, result)

        # Print all leaf nodes
        print_leaf_nodes(root.left, result)
        print_leaf_nodes(root.right, result)

        print_right_perimeter(root.right, result)

    return " ".join(result)


arr = [100, 50, 200, 25, 60, 350, 10, 70, 400]
root = create_BST(arr)
print("\nPrint tree perimeter\n")
print(display_tree_perimeter(root))

# time O(log) and O(n) for worst case
# space O(n)
