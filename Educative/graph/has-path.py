from collections import deque


graph = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": [],
}

## DFS
# def hasPath(graph, src, destination):
#     if src == destination:
#         return True

#     for neighbor in graph[src]:
#         if hasPath(graph, neighbor, destination):
#             return True

#     return False

## BFS
def hasPath(graph, src, destination):
    queue = deque()
    queue.append(src)
    while queue:
        curr = queue.popleft()
        if curr == destination:
            return True

        for neighbor in graph[curr]:
            queue.append(neighbor)

    return False


print(hasPath(graph, "a", "d"))
