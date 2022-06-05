from collections import deque

def bfs(x, y, dir):

    if dir == 0: # 오른쪽 
        dx = [0, 1]    # 아래 오른쪽대각
        dy = [1, 1]
    else:        # 왼쪽
        dx = [0,-1]    # 아래 왼쪽대각
        dy = [1, 1]

    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()

        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and ny >= 0 and nx < N and ny < N:
                if dp[ny][nx] < dp[y][x] + pyramid[ny][nx]:
                    dp[ny][nx] = dp[y][x] + pyramid[ny][nx]

                if (nx,ny) not in queue:
                    queue.append((nx,ny))

    print(max(dp[N-1]))

N = int(input())
pyramid = [list(map(int, input().split())) for i in range(N)]
dp = [[0 for i in range(N)] for i in range(N)]
dp[0] = pyramid[0]

if len(pyramid[0]) == 1:
    dir = 0
else:
    dir = 1 

bfs(len(pyramid[0])-1,0, dir) 