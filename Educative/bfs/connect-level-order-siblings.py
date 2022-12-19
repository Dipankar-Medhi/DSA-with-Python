from collections import deque


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left, self.right, self.next = None, None, None

    # level order traversal using 'next'
    def levelOrderTraversal(self):
        nextLevelRoot = self

        while nextLevelRoot:
            curr = nextLevelRoot
            nextLevelRoot = None

            while curr:
                print(str(curr.value) + "-->", end="")

                if not nextLevelRoot:
                    if curr.left:
                        nextLevelRoot = curr.left
                    elif curr.right:
                        nextLevelRoot = curr.right
                curr = curr.next

            print()


def connectLevelOrderSiblings(root):
    if root is None:
        return

    queue = deque()
    queue.append(root)

    while queue:
        prevNode = None
        levelSize = len(queue)

        # connect nodes of this level
        for _ in range(levelSize):
            currNode = queue.popleft()

            if prevNode:
                prevNode.next = currNode

            prevNode = currNode

            # insert children of curr node in queue
            if currNode.left:
                queue.append(currNode.left)
            if currNode.right:
                queue.append(currNode.right)

    print()


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

connectLevelOrderSiblings(root)

root.levelOrderTraversal()
