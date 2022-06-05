N, M = map(int, input().split())

my_map = []
cctv = [1,2,3,4,5]

global count
count = 0
dx = [1,0,-1,0] # 오른쪽 아래 왼 위
dy = [0,1,0,-1]

for i in range(N):  
    my_map.append(list(map(int, input().split())))

x = 0
y = 0

lst = []
def search(x, y, dir):
    global count
    nx = x + dx[dir]
    ny = y + dy[dir]

    if nx >= 0 and ny >= 0 and nx <M and ny <N and my_map[ny][nx] != 6:
        
        if my_map[ny][nx] in cctv:  # cctv가 cctv를 지나갈 때
            search(nx, ny, dir)
        else:      # 아닌 경우
            count = count + 1
            search(nx, ny ,dir)

def monitor(x,y, dir):
    nx = x + dx[dir]
    ny = y + dy[dir]

    if nx>= 0 and ny >= 0 and nx <M and ny <N and my_map[ny][nx] != 6:

        if my_map[ny][nx] in cctv:
            monitor(nx, ny, dir)
        else:
            my_map[ny][nx] = '#'
            monitor(nx, ny, dir)


def check(my_map):
    count = 0 
    for i in range(N):
        for j in range(M):
            if my_map[i][j] == 0:
                count = count + 1

    return count

lst = []
sum_lst = []


for i in range(N):
    for j in range(M):
        lst = []
        sum_lst = []
        if my_map[i][j] == 1:
            for k in range(4):
                search(j,i,k)
                lst.append(count)
                count = 0
            max_idx = lst.index(max(lst))

        elif my_map[i][j] == 2:
            for k in range(4):
                search(j, i,k)
                lst.append(count)
                count = 0
            parallel = lst[0] + lst[2]
            vertical = lst[1] + lst[3] 

        elif my_map[i][j] == 3:
            for k in range(4):
                search(j,i,k)
                lst.append(count)
                count = 0
            
            first = lst[0] + lst[1]
            second = lst[1] + lst[2]
            third = lst[2] + lst[3]
            fourth = lst[3] + lst[0]

            sum_lst.append(first)
            sum_lst.append(second)
            sum_lst.append(third)
            sum_lst.append(fourth)

            max_num = max(sum_lst)

                    
    
        elif my_map[i][j] == 4:
            for k in range(4):
                search(j,i,k)
                lst.append(count)
                count = 0

            first = lst[0] + lst[1] + lst[2]
            second = lst[1] + lst[2] + lst[3]
            third = lst[2] + lst[3] + lst[0]
            fourth = lst[3] + lst[0] + lst[1]

            sum_lst.append(first)
            sum_lst.append(second)
            sum_lst.append(third)
            sum_lst.append(fourth)

            max_num = max(sum_lst)

        elif my_map[i][j] == 5:
            for k in range(4):
                search(i,j,k)
                
for i in range(N):
        print(my_map[i])
safe_num = check(my_map)           
print(safe_num)

