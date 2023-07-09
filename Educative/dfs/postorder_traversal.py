# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def postorderTraversal(root: TreeNode):
    # Initialize an empty list to store the postorder traversal output.
    output = []

    # Define an inner recursive helper function that performs the postorder traversal.
    def postorder(node: TreeNode) -> None:
        # Base case: if the current node is None, return without doing anything.
        if not node:
            return

        # Recursively traverse the left subtree.
        postorder(node.left)

        # Recursively traverse the right subtree.
        postorder(node.right)

        # Append the value of the current node to the output list.
        output.append(node.val)

    # Call the inner helper function to perform the actual traversal.
    postorder(root)

    # Return the output list.
    return output


root = TreeNode()
root.left = TreeNode(1)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(5)
root.right.right = TreeNode(6)

print(postorderTraversal(root))
