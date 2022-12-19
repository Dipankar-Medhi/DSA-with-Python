def undirected_path(graph, src, target):
    # store the visited nodes in the set
    visited = set()
    return hasPath(graph, src, target, visited)


def hasPath(graph, src, target, visited):

    if src == target:
        return True
    if src in visited:
        return False
    # keeping adding the sources
    visited.add(src)

    for neighbor in graph[src]:
        if hasPath(graph, neighbor, target, visited):
            return True

    return False
