from collections import deque


def is_scheduling_possible(tasks, prerequisites):
    sortedOrder = []
    if tasks <= 0:
        return False

    # set the incoming edges and the graph
    inDegree = {i: 0 for i in range(tasks)}
    graph = {i: [] for i in range(tasks)}

    # build the graph or the adjacency list
    for prerequisite in prerequisites:
        parent, child = prerequisite[0], prerequisite[1]
        # add to the list
        graph[parent].append(child)
        # add the edges for the children
        inDegree[child] += 1

    print(inDegree, graph)

    # find the sources i.e all nodes with 0 degrees
    sources = deque()
    for key in inDegree:
        if inDegree[key] == 0:
            sources.append(key)

    # now add the soruces to the sortedOrder arr and substract
    # 1 edge from its children. And if the in-degree
    # of the children becomes 0, add it to the sources queue
    while sources:
        source = sources.popleft()
        sortedOrder.append(source)
        for child in graph[source]:
            inDegree[child] -= 1
            if inDegree[child] == 0:
                sources.append(child)

    # if sortedorder doesn't contain all tasks, that measn there is a cycle, so the tasks
    # can't be scheduled
    return len(sortedOrder) == tasks


print(is_scheduling_possible(3, [[0, 1], [1, 2]]))
