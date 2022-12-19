def connected_components_count(graph):
    count = 0
    visited = set()  # keep track of the visited nodes

    for node in graph:
        if explore(graph, node, visited):
            count += 1

    return count


def explore(graph, curr_node, visited):
    if curr_node in visited:
        return False

    visited.add(curr_node)

    for neighbor in graph[curr_node]:
        explore(graph, neighbor, visited)

    return True


graph = {
    0: [8, 1, 5],
    1: [0],
    5: [0, 8],
    8: [0, 5],
    2: [3, 4],
    3: [2, 4],
    4: [3, 2],
}
print(connected_components_count(graph))
