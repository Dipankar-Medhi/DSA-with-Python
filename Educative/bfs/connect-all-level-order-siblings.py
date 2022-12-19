from collections import deque


class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left, self.right, self.next = None, None, None

    # tree traversal using 'next pointer
    def printLevelOrder(self):
        curr = self
        while curr:
            print(str(curr.val) + " ", end='')
            curr = curr.next


def connectAllLevelOrderSiblings(root):
    if root is None:
        return

    queue = deque()
    queue.append(root)

    currNode, prevNode = None, None

    while queue:
        currNode = queue.popleft()
        if prevNode:
            prevNode.next = currNode
        prevNode = currNode

        # add childrens to queue
        if currNode.left:
            queue.append(currNode.left)
        if currNode.right:
            queue.append(currNode.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

connectAllLevelOrderSiblings(root)

root.printLevelOrder()
