
graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}

def dfs(graph, source):
    stack = [source]
    result = []

    while stack:
        curr = stack.pop()
        result.append(curr)

        # put neighbors in stack
        for neighbor in graph[curr]:
            stack.append(neighbor)
        
    return result

print(dfs(graph, 'a'))