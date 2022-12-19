from collections import deque


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left, self.right = None, None


def levelOrderSuccesor(root, key):

    if root is None:
        return None

    queue = deque()
    queue.append(root)

    while queue:
        currNode = queue.popleft()

        # add its children to the queue
        if currNode.left:
            queue.append(currNode.left)
        if currNode.right:
            queue.append(currNode.right)

        # break if key matched
        if currNode.value == key:
            break

    return queue[0].value if queue else None


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.left = Node(6)
root.right.right = Node(7)


print(levelOrderSuccesor(root, 3))
