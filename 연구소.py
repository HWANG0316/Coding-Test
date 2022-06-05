import copy
import itertools

global temp
temp = []
dx = [-1,1,0,0] # 왼쪽 오른쪽 위 아래
dy = [0,0,-1,1]

N, M = map(int, input().split())
my_map = [[0 for i in range(M)] for i in range(N)]

safe_area_list = []

for i in range(N):
    my_map[i] = list(map(int, input().split()))

def dfs(x , y):  # 탐색하기 
    global temp

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and ny >= 0 and nx < M and ny <N and temp[ny][nx] == 0:
            temp[ny][nx] = 2
            dfs(nx, ny) 
    
def find_virus(my_map):                                      # 바이러스 위치 찾기

    result = []
    for i in range(N):
        for j in range(M):
            if my_map[i][j] == 2:
                result.append([i,j])
    return result

def find_combination(index_list):
    result = list(itertools.combinations((index_list),3))    # 조합 생성하기
    return result
    
def find_index(my_map):                     # 비어있는 곳의 인덱스 찾기 (벽을 어디에 세울지 알기 위해서)
    index_list = []
    for i in range(N):
        for j in range(M):
            if my_map[i][j] == 0:
                index_list.append([i,j])

    return index_list

def build_wall(my_map, combination_list):    # 벽 세워서 점검하기 
    global temp
    result = find_virus(my_map)

    for i in range(len(combination_list)):
        temp = copy_map(my_map)

        wall_1st = combination_list[i][0]
        wall_2nd = combination_list[i][1]
        wall_3rd = combination_list[i][2]
        
        temp[wall_1st[0]][wall_1st[1]] = 1
        temp[wall_2nd[0]][wall_2nd[1]] = 1
        temp[wall_3rd[0]][wall_3rd[1]] = 1

        for i in range(len(result)):
            x = result[i][1]
            y = result[i][0]
            dfs(x,y)
        
        safe_area = count_safe_area(temp)
        safe_area_list.append(safe_area)

def count_safe_area(my_map):    # 안전 영역 세기

    result = 0
    for i in range(N):
        result = result + my_map[i].count(0)
    return result

def copy_map(my_map):
    temp = copy.deepcopy(my_map)    # my_map copy  
    return temp


index_list = find_index(my_map)   # 비어있는 곳의 i, j 인덱스 찾기 
combination_list = find_combination(index_list)      # 찾은 index로 조합 생성하기
build_wall(my_map, combination_list)
print(max(safe_area_list))