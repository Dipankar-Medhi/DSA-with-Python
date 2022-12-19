from collections import deque


graph = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": [],
}


def bfs(graph, source):
    queue = deque()
    queue.append(source)
    result = []

    while queue:
        curr = queue.popleft()
        result.append(curr)

        # put neighbors in queue
        for neighbor in graph[curr]:
            queue.append(neighbor)

    return result


print(bfs(graph, "a"))
