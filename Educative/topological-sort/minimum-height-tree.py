from collections import deque


def find_trees(nodes, edges):
    if nodes <= 0:
        return []

    if nodes == 1:
        return [0]

    # initialize graph
    inDegree = {i: 0 for i in range(nodes)}
    graph = {i: [] for i in range(nodes)}

    # build the graph
    for edge in edges:
        n1, n2 = edge[0], edge[1]

        # for undirected graph
        graph[n1].append(n2)
        graph[n2].append(n1)

        inDegree[n1] += 1
        inDegree[n2] += 1

    print(inDegree, graph)

    # find all leaves i.e nodes with 1 in degree
    leaves = deque()
    for key in inDegree:
        if inDegree[key] == 1:
            leaves.append(key)

    # remove leaves level by level and substract each leave's childern indegree
    totalNodes = nodes
    while totalNodes > 2:
        leaveSize = len(leaves)
        totalNodes -= leaveSize
        for i in range(leaveSize):
            leaf = leaves.popleft()
            # decrement child node in degree
            for child in graph[leaf]:
                inDegree[child] -= 1
                if inDegree[child] == 1:
                    leaves.append(child)

    return list(leaves)


print(find_trees(4, [[0, 1], [0, 2], [2, 3]]))
