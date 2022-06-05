def dfs(graph, start, visited):
    visited[start] = 1
    for i in graph[start]:
        if visited[i] != 1:
            visited[i] = 1
            dfs(graph, i, visited)

def solution(n, computers):    
    visited = [0 for i in range(n + 1)]
    graph = [[] for i in range(n + 1)]
    
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and i != j:
                graph[i + 1].append(j + 1)
    count  = 0 
    for i in range(1, n + 1):
        if visited[i] != 1:
            dfs(graph, i, visited)
            count = count + 1
    
    return count
        


print(solution(3,	[[1, 1, 0], [1, 1, 0], [0, 0, 1]]), 2)
print(solution(3,	[[1, 1, 0], [1, 1, 1], [0, 1, 1]]), 1)