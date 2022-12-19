from collections import deque


def shortest_path(graph, src, destination):
    # we keep track of the visited nodes
    queue = deque()
    queue.append((src, 0))  # (source, distance)

    visited = set()
    visited.add(src)

    while queue:
        node, dist = queue.popleft()

        if node == destination:
            return dist

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append((neighbor, dist + 1))
                visited.add(node)


graph = {
    0: [8, 1, 5],
    1: [0],
    5: [0, 3],
    8: [0, 5],
    2: [3, 4],
    3: [2, 5],
    4: [3, 2],
}
print(shortest_path(graph, 0, 3))
