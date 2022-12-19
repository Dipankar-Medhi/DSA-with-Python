

from collections import deque


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None


def reverselevelOrderTraversal(root):
    result = deque()
    # return if root is null
    if root is None:
        return result

    queue = deque()
    # add root to queue
    queue.append(root)

    while queue:
        levelSize = len(queue)

        currLevel = []
        # for every element in the queue
        for _ in range(levelSize):
            currNode = queue.popleft()
            # add the left element to the arr
            currLevel.append(currNode.value)
            # add its children to the queue
            if currNode.left:
                queue.append(currNode.left)
            if currNode.right:
                queue.append(currNode.right)

        result.appendleft(currLevel)

    return result


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print(reverselevelOrderTraversal(root))
