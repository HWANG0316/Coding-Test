from collections import deque

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(x,y, maps):
    
    N = len(maps)   # 행 
    M = len(maps[0]) # 열
    queue = deque()
    queue.append((y,x))
    visited = [[0 for i in range(M)] for j in range(N)]
    visited[0][0] = 1
    
    while queue:
        
        y,x = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx >= 0 and ny >= 0 and nx < M and ny < N and maps[ny][nx] == 1 and visited[ny][nx] == 0:
                maps[ny][nx] = maps[y][x] + 1
                visited[ny][nx] = 1
                queue.append((ny,nx))

            if ny == N-1 and nx == M-1:
                return maps[ny][nx]
    
    return -1

def solution(maps):
    
    result = bfs(0,0,maps)
    print(result)
    return result