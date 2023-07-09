# Definition for a binary tree node.

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderTraversal(root: TreeNode) -> List[int]:
    # Initialize an empty list to store the inorder traversal output.
    output = []

    # Define an inner recursive helper function that performs the inorder traversal.
    def inorder(node: TreeNode) -> None:
        # Base case: if the current node is None, return without doing anything.
        if not node:
            return

        # Recursively traverse the left subtree.
        inorder(node.left)

        # Append the value of the current node to the output list.
        output.append(node.val)

        # Recursively traverse the right subtree.
        inorder(node.right)

    # Call the inner helper function to perform the actual traversal.
    inorder(root)

    # Return the output list.
    return output

root = TreeNode()
root.left = TreeNode(1)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(5)
root.right.right = TreeNode(6)

print(inorderTraversal(root))

