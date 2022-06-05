dx = [1,0,-1,0]
dy = [0,1,0,-1]

def solution(dirs):
    visited = [[0 for i in range(11)] for j in range(11)]
    x, y = 5, 5
    count = 0
    visited[y][x] = 1
    lst = []
    for i in dirs:
        if i == 'R':
            i = 0
        elif i == 'D':
            i = 1
        elif i == 'L':
            i = 2
        elif i == 'U':
            i = 3
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and ny >= 0 and nx < 11 and ny < 11:
            if visited[ny][nx] == 0:
                lst.append([ny,nx, y, x])
                visited[ny][nx] = 1
                count = count + 1
            elif visited[ny][nx] == 1 and [ny,nx,y,x] not in lst and [y,x,ny,nx] not in lst:
                lst.append([ny,nx, y, x])
                count = count + 1
            y, x = ny, nx
        
    return count