
class Graph:
    def __init__(self, adjList=None):
        if adjList is None:
            adjList = []
        self.adjList = adjList

    def bfs(self, graph, root):
        queue = [root]
        enqueued = {root}

        i = 0
        while i < len(queue):
            popped = queue[i]
            i += 1
            print(popped)
            for neighbour in graph.adjList[popped]:
                if neighbour not in enqueued:
                    queue.append(neighbour)
                    enqueued.add(neighbour)
