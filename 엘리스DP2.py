from collections import deque

N, M = map(int, input().split())
mymap = [list(map(int,input().split())) for i in range(N)]
dp = [[0 for i in range(M)] for j in range(N)]

dx = [1, 0]
dy = [0, 1]
dp[0][0] = mymap[0][0]

def bfs(nx, ny):
    queue = deque()
    queue.append((nx,ny))

    while queue:
        x, y = queue.popleft()

        for i in range(2):
            nx = x + dx[i]
            ny = y  +dy[i]

            if nx >= 0 and ny >= 0 and nx < M and ny < N:

                if dp[ny][nx] < dp[y][x] + mymap[ny][nx]:
                    dp[ny][nx] = dp[y][x] + mymap[ny][nx]
                
                if (nx,ny) not in queue:
                    queue.append((nx,ny))

bfs(0,0)
print(dp[M-1][N-1])



