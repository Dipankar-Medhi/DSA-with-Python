# using queue we traverse the tree

class Tree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def bfs(self, root):
        if root is None:
            return
        queue = [root]
        i = 0
        while i < len(queue):
            popped = queue[i]
            i += 1
            print(popped.data)
            if popped.left is not None:
                queue.append(popped.left)
            if popped.right is not None:
                queue.append(popped.right)


tr = Tree([20, 40, 50])
tr.bfs(40)
