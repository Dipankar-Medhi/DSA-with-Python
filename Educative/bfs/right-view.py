from collections import deque


class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left, self.right = None, None


def rightView(root):
    result = []

    if root is None:
        return result

    queue = deque()
    queue.append(root)

    while queue:
        levelSize = len(queue)

        for i in range(0, levelSize):
            currNode = queue.popleft()
            # add the last node of the level
            if i == levelSize - 1:
                result.append(currNode.val)

            # add children to the queue
            if currNode.left:
                queue.append(currNode.left)
            if currNode.right:
                queue.append(currNode.right)

    return result


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.left = Node(6)
root.right.right = Node(7)

print(rightView(root))
