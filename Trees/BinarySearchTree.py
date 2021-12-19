"""
Binary search tree reduces the search space by 1/2.
So, the time complexion is O(logn)

BST are basically set, it removes duplicate elements.

### the left node is less than < root
### the right node is more than > root

Traversal Techniques:-
1. In Order traversal = Left tree -> Root -> Right tree
2. Pre Order traversal = Root -> Left tree -> Right tree
3. Post Order traversal = Left tree -> Right tree -> Root

"""


class BinarySearchTreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:
            # add data in the left subtree
            if self.left:
                self.left.add_child(data)
            else:
                # when left is empty, just add left subtree
                self.left = BinarySearchTreeNode(data)
        else:
            # add data in right subtree
            if self.right:
                self.right.add_child(data)
            else:
                # when right is empty, just add right subtree
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):
        elements = []

        # visit left tree
        if self.left:
            elements += self.left.in_order_traversal()

        # visit root
        elements.append(self.data)

        # visit right tree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def find_max(self):
        if self.right == None:
            return self.data
        else:
            return self.right.find_max()

    def find_min(self):
        if self.left == None:
            return self.data
        else:
            return self.right.find_min()

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
            else:
                return None
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
            else:
                return None
        else:
            if self.left == None and self.right == None:
                return None
            if self.left == None:
                return self.right
            if self.right == None:
                return self.right
            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)
        return self

    def search(self, val):
        if self.data == val:
            return True
        if val < self.data:
            # val midht be in left subtree
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            # val might be in right subtree
            if self.right:
                return self.right.search(val)
            else:
                return False


def buildTree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


elements = [17, 4, 5, 12, 9, 1, 2, 20, 22, 36, 18]
tree = buildTree(elements)
print(tree.in_order_traversal())
tree.delete(12)
print(tree.in_order_traversal())

