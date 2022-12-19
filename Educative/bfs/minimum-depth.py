from collections import deque


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None


def min_depth(root):
    # return if root is null
    if root is None:
        return root

    queue = deque()
    # add root to queue
    queue.append(root)
    minDepth = 0

    while queue:
        minDepth += 1
        levelSize = len(queue)

        # for every element in the queue
        for _ in range(levelSize):
            currNode = queue.popleft()

            # check if it is leaf node
            if not currNode.left and not currNode.right:
                return minDepth

            # add its children to the queue
            if currNode.left:
                queue.append(currNode.left)
            if currNode.right:
                queue.append(currNode.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.left = Node(6)
root.right.right = Node(7)

print(min_depth(root))
