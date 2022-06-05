import copy

N, M = map(int, input().split())
current_y , current_x , direction = map(int, input().split())

my_map = [[0 for i in range(M)] for i in range(N)]

for i in range(N):
    my_map[i] = list(map(int, input().split()))

def search(x, y, direction):  # 탐색
    
    dx, dy = set_dxdy(direction)
    count = 0
    for i in range(4):  # for문이 돌아간다5는건 2단계로 돌아왔다는 것과 동일.
        nx = x + dx[i]
        ny = y + dy[i]
            
        if nx >= 0 and ny >= 0 and nx < M and ny <N and my_map[ny][nx] == 0:
            direction = set_direction(direction, i)
            clear(nx, ny, direction)   # 1단계로 돌아가기.
            break
        elif nx >= 0 and ny >= 0 and nx < M and ny <N and (my_map[ny][nx] == 1 or my_map[ny][nx] == "C"):
            count = count + 1

    nx = x + dx[1]
    ny = y + dy[1]
    if count == 4 and my_map[ny][nx] == 1:
        return
    elif count ==4 and my_map[ny][nx] != 1:   # 2단계로 돌아가기 
        search(nx, ny, direction)

def clear(x, y, direction):

    if my_map[y][x] == 0:     # 청소해야 할 때
        my_map[y][x] = "C"
    
    search(x, y, direction)

def set_direction(direction, i):

    if direction == 0:
        if i == 0:
            direction = 3
        elif i == 1:
            direction = 2
        elif i == 2:
            direction = 1
        elif i == 3:
            direction = 0
    elif direction == 1:
        if i == 0:
            direction = 0
        elif i == 1:
            direction = 3
        elif i == 2:
            direction = 2
        elif i == 3:
            direction = 1
    elif direction == 2:
        if i == 0:
            direction = 1
        elif i == 1:
            direction = 0
        elif i == 2:
            direction = 3
        elif i == 3:
            direction = 2
    elif direction == 3:
        if i == 0:
            direction = 2
        elif i == 1:
            direction = 1
        elif i == 2:
            direction = 0
        elif i == 3:
            direction = 3

    return direction
    

def set_dxdy(direction):
    if direction == 0:     # 북 
        dx = [-1,0,1,0]
        dy = [0,1,0,-1]
    elif direction == 1:   # 동 
        dx = [0,-1,0,1]
        dy = [-1,0,1,0]
    elif direction == 2:   # 남
        dx = [1,0,-1,0]
        dy = [0,-1,0,1]
    elif direction == 3:   # 서
        dx = [0,1,0,-1]
        dy = [1,0,-1,0]

    return dx, dy

def count_clear_area(my_map):

    result = 0

    for i in range(N):
        count = my_map[i].count("C")
        result = result + count

    print(result)

clear(current_x, current_y, direction)
count_clear_area(my_map)