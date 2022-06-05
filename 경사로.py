N, L = map(int, input().split())
my_map = [[0 for i in range(N)] for i in range(N)]

global path
path = 0                   # 지나갈 수 있는 길의 개수 

for i in range(N):
    my_map[i] = list(map(int, input().split()))

def check():  # map check
    global path

    for i in range(N):  # 점검

        build_map = [0 for i in range(N)]
        first = 0
        second = 1

        for j in range(N-1):
            if height_check(my_map[i], first, second) == True:    # 높이가 같을 때
                
                first = first + 1
                second = second + 1

                if first == (N-1):                                # 지나갈 수 있는 길이라고 판단될 때
                    path = path + 1

            else:                                                 # 높이가 다를 때
                
                if build_check(my_map[i], first, second, build_map) == True:                         # 경사로를 놓을 수 있을 때
    
                    first = first + 1
                    second = second + 1

                    if first == (N-1):                            # 지나갈 수 있는 길이라고 판단될 때
                        path = path + 1
                else:                                             # 경사로를 놓지 못할 때
                    break

def height_check(my_map, first, second):
    
    if my_map[first] == my_map[second]:
        return True
    elif abs(my_map[first] - my_map[second]) >= 1:
        return False

def build_check(my_map, first, second, build_map):
    
    if my_map[first] < my_map[second] and abs(my_map[first] - my_map[second]) == 1:      # 왼쪽 값이 오른쪽 값보다 작고 차이가 1이라면 check 

        for i in range(L):                                    # map을 벗어나지 않는 선에서 경사로가 건설되어 있는지, 아닌지 점검 후 진행 
            if build_map[first - i] == 0 and (first - L + 1) >= 0:
                continue
            else:
                return False

        if (first-L + 1) >=0:             # map을 벗어나지 않을 때
            
            for i in range(first - L + 1, first):
                if height_check(my_map,i,i+1) != True:
                    return False

            for i in range(L):
                build_map[first - i] = 1
            return True
        else:
            return False                  # map을 벗어나서 경사로를 놓지 못함
    
    elif my_map[first] > my_map[second] and abs(my_map[first] - my_map[second]) == 1:   # 왼쪽 값이 오른쪽 값보다 크고 차이가 1이라면 check


        for i in range(L):                                          # map을 벗어나지 않는 선에서 경사로가 건설되어 있는지, 아닌지 점검 후 진행
            if build_map[second + i] == 0 and (second + L -1) < N:
                continue
            else:
                return False           # 이미 동일한 자리에 건설되어 있거나 맵을 벗어난다면 False 반환

        if (second + L - 1) <N:           # map을 벗어나지 않을 때

            for i in range(second, second + L - 1):
                if height_check(my_map,i,i+1) != True:
                    return False
            
            for i in range(L):
                build_map[second + i] = 1
            return True        
        else:
            return False                  # map을 벗어나서 경사로를 놓지 못함

def rotate(my_map):   # map rotate

    temp = [[0 for i in range(N)] for i in range(N)]
    
    for i in range(N):
        for j in range(N):
            temp[i][j] = my_map[j][N-i-1]

    return temp 

check()   # 기존 맵 우선적으로 check
my_map = rotate(my_map)        # map 회전
check()   # 회전 시킨 맵 check
print(path)