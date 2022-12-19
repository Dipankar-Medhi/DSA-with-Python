

from collections import deque


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None


def zigzagTraversal(root):
    result = []
    # return if root is null
    if root is None:
        return result

    queue = deque()
    # add root to queue
    queue.append(root)
    leftToright = True

    while queue:
        levelSize = len(queue)

        currLevel = deque()
        # for every element in the queue
        for _ in range(levelSize):

            currNode = queue.popleft()

            if leftToright:
                # add the left element to the arr
                currLevel.append(currNode.value)
            else:
                currLevel.appendleft(currNode.value)

            # add its children to the queue
            if currNode.left:
                queue.append(currNode.left)
            if currNode.right:
                queue.append(currNode.right)

        result.append(list(currLevel))

        leftToright = not leftToright

    return result


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print(zigzagTraversal(root))
