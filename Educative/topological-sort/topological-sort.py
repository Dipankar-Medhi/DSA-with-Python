from collections import deque
"""

def topological_sort(vertices, edges):
    sortedOrder = []

    if vertices <= 0:
        return sortedOrder

    # Initialize the graph
    inDegree = {i: 0 for i in range(vertices)}
    graph = {i: [] for i in range(vertices)}

    # build the graph
    for edge in edges:
        parent, child = edge[0], edge[1]
        # put the child into its parent's list
        graph[parent].append(child)
        # increment child's inDegree (incoming edges)
        inDegree[child] += 1
    print("Graph:", graph, end="\n")
    print("inDegree:", inDegree, end="\n")
    # find all sources i.e, all vertices with 0 inDegrees
    sources = deque()
    for key in inDegree:
        if inDegree[key] == 0:
            sources.append(key)

    # for each source, add to the sorted order and substract 1 from all its children's in degree
    while sources:
        vertex = sources.popleft()
        sortedOrder.append(vertex)
        # get the node's children to decrement their indegree
        for child in graph[vertex]:
            inDegree[child] -= 1
            # add the child that has 0 indegree to the sources
            if inDegree[child] == 0:
                sources.append(child)

    # for cyclic graph
    if len(sortedOrder) != vertices:
        return []

    return sortedOrder


# Time O(V + E) -- V = no of vertices, E = no of edges


print(topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]]))
"""

"""
    class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {c:[] for c in range(numCourses)}
        for course, pre in prerequisites:
            prereq[course].append(pre)
        print(prereq)
        stack = []
        visited, cycle = set(), set()

        def dfs(course):
            if course in cycle:
                return False 
            if course in visited:
                return True 
            
            cycle.add(course)
            for pre in prereq[course]:
                if dfs(pre) == False: 
                    return False 
            
            cycle.remove(course)
            visited.add(course)
            stack.append(course)

            return True 

        for course in range(numCourses):
            if dfs(course) == False:
                return []
        return stack  

"""

from collections import deque

def topological_sort(graph):
    # Step 1: Initialize variables
    result = []  # Stores the sorted nodes
    incoming_edges = {node: 0 for node in graph}  # Count of incoming edges for each node
    queue = deque()  # Queue to store nodes with no incoming edges

    # Step 2: Calculate incoming edges for each node
    for node in graph:
        for neighbor in graph[node]:
            incoming_edges[neighbor] += 1

    # Step 3: Find nodes with no incoming edges and add them to the queue
    for node in graph:
        if incoming_edges[node] == 0:
            queue.append(node)

    # Step 4: Process the nodes in the queue
    while queue:
        node = queue.popleft()
        result.append(node)

        # Step 5: Remove the node and update incoming edges of its neighbors
        for neighbor in graph[node]:
            incoming_edges[neighbor] -= 1
            if incoming_edges[neighbor] == 0:
                queue.append(neighbor)

    # Step 6: Check for cycles
    if len(result) != len(graph):
        # If there are cycles, the graph is not a directed acyclic graph (DAG)
        return []

    return result


# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': ['E'],
    'E': []
}

sorted_nodes = topological_sort(graph)
print(sorted_nodes)
