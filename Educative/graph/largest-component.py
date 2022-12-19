def largestComponent(graph):
    largest = 0
    visited = set()

    for node in graph:
        size = explore(graph, node, visited)
        largest = max(size, largest)

    return largest


def explore(graph, node, visited):
    if node in visited:
        return 0

    visited.add(node)

    # every node of size 1
    size = 1
    for neighbor in graph[node]:
        size += explore(graph, neighbor, visited)

    return size


graph = {
    0: [8, 1, 5],
    1: [0],
    5: [0, 8],
    8: [0, 5],
    2: [3, 4],
    3: [2, 4],
    4: [3, 2],
}
print(largestComponent(graph))
