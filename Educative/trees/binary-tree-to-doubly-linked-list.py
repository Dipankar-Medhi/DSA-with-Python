# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Definition for a doubly-linked list node.
class ListNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class Solution:
    def binaryToDoublyLinkedList(self, root: TreeNode) -> ListNode:
        if not root:
            return None

        # recursively convert left subtree
        left_head = self.binaryToDoublyLinkedList(root.left)

        # create doubly linked list node for current node
        curr_node = ListNode(root.val)

        if left_head:
            # set current node's left pointer to last node of left subtree
            left_tail = left_head
            while left_tail.next:
                left_tail = left_tail.next
            curr_node.prev = left_tail
            left_tail.next = curr_node

        # recursively convert right subtree
        right_head = self.binaryToDoublyLinkedList(root.right)

        if right_head:
            # set current node's right pointer to first node of right subtree
            curr_node.next = right_head
            right_head.prev = curr_node

        # return head of doubly linked list
        if left_head:
            return left_head
        else:
            return curr_node


# example usage
if __name__ == "__main__":
    # create a sample binary tree
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right = TreeNode(5)
    root.right.right = TreeNode(6)

    # convert binary tree to doubly linked list
    solution = Solution()
    head = solution.binaryToDoublyLinkedList(root)

    # print out the doubly linked list
    node = head
    while node:
        print(node.val, end=" ")
        node = node.next
    print()
