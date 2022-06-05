from collections import deque

def solution(n, edge):
    my_map = [[0 for i in range(n)] for j in range(n)]
    dist = [0 for i in range(n)]
    visited = []
    for i, j in edge:
        my_map[i-1][j-1] = 1
        my_map[j-1][i-1] = 1 

    queue = deque()
    queue.append((0,0))  # 시작 노드 추가

    while queue:
        x, y = queue.popleft()
        for i in range(n):
            nx = i             # x축만 움직이면서 확인하면 됨
            ny = y

            if nx >= 0 and ny >= 0 and nx < n and ny < n and my_map[ny][nx] == 1 and (nx, nx) not in queue and nx not in visited:
                queue.append((nx,nx))
                
                if dist[nx] == 0:
                    dist[nx] = dist[ny]  + 1
                else:
                    dist[nx] = min(dist[nx], my_map[y][x] + dist[nx])

        visited.append(y)
    result = dist.count(max(dist))
    return result

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