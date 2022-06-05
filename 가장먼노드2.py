from collections import deque

def solution(n, edge):
    graph = [[] for i in range(n + 1)]
    visited = [0 for i in range(n + 1)]
    dist = [ 0 for i in range(n + 1)]
    start = 1

    for i, j in edge:
        graph[i].append(j)
        graph[j].append(i)
    
    queue = deque()
    queue.append(start)

    visited[start] = 1
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if visited[i] != 1:
                dist[i] = dist[v] + 1
                visited[i] = 1
                queue.append(i)

    return dist.count(max(dist))

print(solution(6,	[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]), 3)
print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]), 3)
print(solution(11, [[1, 2], [1, 3], [2, 4], [2, 5], [3, 5], [
      3, 6], [4, 8], [4, 9], [5, 9], [5, 10], [6, 10], [6, 11]]), 4)
print(solution(4, [[1, 2], [2, 3], [3, 4]]), 1)
print(solution(2, [[1, 2]]), 1)
print(solution(5, [[4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]), 2)
print(solution(4, [[1, 2], [1, 3], [2, 3], [2, 4], [3, 4]]), 1)
print(solution(4, [[1, 4], [1, 3], [2, 3], [2, 1]]), 3)
print(solution(4, [[3, 4], [1, 3], [2, 3], [2, 1]]), 1)
print(solution(4, [[4, 3], [1, 3], [2, 3]]), 2)