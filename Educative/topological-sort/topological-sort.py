from collections import deque


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
