from collections import deque

dx = [1,0,-1,0] # 오른쪽 아래 왼쪽 위
dy = [0,1,0,-1]
def bfs(x,y):

    queue = deque()
    queue.append((x,y))
    visited[y][x] = 1
    while queue:

        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and ny >= 0 and nx < N and ny < N and mymap[ny][nx] != 0 and visited[ny][nx] != 1:
                
                visited[ny][nx] = 1
                if dp[ny][nx] < dp[y][x] + mymap[ny][nx]:
                    dp[ny][nx] = dp[y][x] + mymap[ny][nx]

                if ny == N-1 and nx == N-1:
                    return dp[ny][nx]
                    
                if (nx, ny) not in queue:
                    queue.append((nx,ny))

        
N = int(input())
mymap = [list(map(int, input())) for i in range(N)]
visited = [[0 for i in range(N)] for j in range(N)]
dp = [[0 for i in range(N)] for j in range(N)]
dp[0][0] = mymap[0][0]

result = bfs(0,0)
print(result)
