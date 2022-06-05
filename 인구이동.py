# 인구 차이가 L명 이상 R명 이하라면 국경선 오픈    com
# 위 조건에 의해 국경선이 열렸다면 인구 이동 시작
# 인접한 칸만을 이동할 수 있으면 연합이라고 부름
# 연합을 이루고 있는 칸의 인구수는 ~~
# 연합 해체하고 국경선 닫음
import copy
import sys

sys.setrecursionlimit(10**7)
global result
global check_map


dx = [1, -1, 0,  0] # 오른쪽 왼쪽 아래 위
dy = [0,  0, 1, -1]  
my_map = []
visited = []
check_complete_map = []
check_map = []
result = 0

def check(temp_map, check_map):

    for i in range(N):
        for j in range(N):
            if temp_map[i][j] != check_map[i][j]:
                return False

    return True

def move(my_map, check_map, result_list, num_list):
    count = 0
    
    for k in range(len(num_list)):
        num = num_list[k]
        result = result_list[k]
        count = 0

        for i in range(N):
            for j in range(N):
                if check_map[i][j] == num:
                    count = count + 1


        for i in range(N):
            for j in range(N):
                if check_map[i][j] == num:
                    my_map[i][j] = result // count
    return my_map        

def dfs(x, y, num, start):
    global result
    global check_map
 
    if visited[y][x] != 1:
        visited[y][x] = 1
    else:
        return

    for i in range(4):

        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and ny >= 0 and nx < N and ny < N and check_map[ny][nx] == 0 and visited[ny][nx] != 1:

            result_sum = abs(my_map[y][x] - my_map[ny][nx])

            if result_sum >= L and result_sum <= R:
                result = result + my_map[ny][nx]
                check_map[y][x] = num
                check_map[ny][nx] = num    
                dfs(nx, ny, num, start)

def num_sum(check_map, num):
    
    result = 0
    for i in range(N):
        for j in range(N):
            
            if check_map[i][j] == num:
                result = result + my_map[i][j]
      
    return result

N, L, R = map(int, input().split())
result = 0

visited = [[0 for k in range(N)] for l in range(N)]
for i in range(N):
    my_map.append(list(map(int, input().split())))

for k in range(0, 2000):
    
    check_complete_map = copy.deepcopy(my_map)
    check_map = [[0 for k in range(N)] for l in range(N)]
    visited = [[0 for k in range(N)] for l in range(N)]
    
    result_list = []
    num_list = []

    num = 1
    result = 0
    
    for i in range(N):
        for j in range(N):
            
            if visited[i][j] != 1:
                start = my_map[i][j]    
                dfs(j, i, num, start)

                if result != 0:
                    result = result + start
                    result_list.append(result)
                    num_list.append(num)
                    num = num + 1
                    result = 0
            

    move(my_map, check_map, result_list, num_list) 

    if check(check_complete_map, my_map)  == True:
        print(k)
        break



# 시간 초과 관련 문제가 존재한다. 아직까지 해결 방법을 찾지 못하였다.