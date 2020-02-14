def recursive_dfs(a):
    if a not in visited:
        visited.append(a)
    for i in graph[a]:
        if i not in visited:
            recursive_dfs(i)
    return visited
visited = []
graph = {'A': set(['B', 'C', 'E']),
         'B': set(['A', 'D', 'F']),
         'C': set(['A', 'G']),
         'D': set(['B']),
         'E': set(['A', 'F']),
         'F': set(['B']),
         'G': set(['G'])}

root = 'B'
print(recursive_dfs(root))


