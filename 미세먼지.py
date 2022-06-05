import copy

R, C, T = map(int, input().split())

my_map = []

dx_list = [[1, 0, -1, 0], [1, 0, -1, 0]]  # 오른 위 왼 아래 -> 반시계 [0] 
dy_list = [[0, -1, 0, 1], [0, 1, 0, -1]]  # 오른 아래 왼 위 ->   시계 [1]

for i in range(R):
    my_map.append(list(map(int, input().split())))

def spread(my_map):

    temp_map = [[0 for i in range(C)] for j in range(R)] #  temp map
    
    for i in range(R):
        for j in range(C):

            if my_map[i][j] != 0 and my_map[i][j] != -1:
                dir_count = 0
                spread_mount = int(my_map[i][j] / 5)  # spread mount 

                for k in range(4):
                    nx = j + dx_list[0][k]   # 시계 반시계 상관없음
                    ny = i + dy_list[0][k]

                    if nx>=0 and ny>=0 and nx < C and ny < R and my_map[ny][nx] != -1:
                        dir_count = dir_count + 1
                        temp_map[ny][nx] = temp_map[ny][nx] + spread_mount
                
                temp_map[i][j] = temp_map[i][j] + my_map[i][j] - spread_mount * dir_count 

            if my_map[i][j] == -1:
                temp_map[i][j] = -1
    my_map = copy.deepcopy(temp_map)

    return my_map

def find_machine():
    m_pos = []
    for i in range(R):
        for j in range(C):
            if my_map[i][j] == -1:
                m_pos.append([i,j + 1])
    return m_pos

def remain():
    result = 0
    for i in range(R):
        result = result + sum(my_map[i])

    result = result + 2
    return result
def circulate(x, y, direction):

    dx = dx_list[direction]
    dy = dy_list[direction]

    copymap = copy.deepcopy(my_map)

    my_map[y][x] = 0

    i = 0    
    while(i != 4):
        nx = x + dx[i]    
        ny = y + dy[i]  
        
        if nx >=0 and ny >=0 and nx < C and ny < R and my_map[ny][nx] != -1: 
            my_map[ny][nx] = copymap[y][x]
            x = nx
            y = ny
        else:
            i = i + 1

m_pos = find_machine()

for i in range(T):
    my_map = spread(my_map)
    circulate(m_pos[0][1],m_pos[0][0], 0)
    circulate(m_pos[1][1],m_pos[1][0], 1)

print(remain())