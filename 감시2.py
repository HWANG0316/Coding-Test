dx = [1, 0, -1,  0]  # 오른쪽 아래 왼쪽 위
dy = [0, 1,  0, -1]

def dfs(x, y, dir):
    nx = x + dx[dir]
    ny = y + dy[dir]

    if nx >= 0 and ny >= 0 and nx < M and ny < N and my_map[ny][nx] != 6:
        if my_map[ny][nx] == 0:
            my_map[ny][nx] = '#'
        dfs(nx, ny)

def check(my_map, num, y,x):
    if num == 5:
        dfs(x,y)

my_map = []
camera = []                        # camera  - > (numbering, y, x)
N, M = map(int, input().split())

for i in range(N):                                      # map generate
    my_map.append(list(map(int, input().split())))


for i in range(N):  
    for j in range(M):
        if my_map[i][j] != 0 and my_map[i][j] != 6:
            camera.append([my_map[i][j], i, j])
camera.sort(key = lambda x:x[0], reverse = True)

for num, y, x in camera:
    check(my_map,num,y,x)

print(my_map)