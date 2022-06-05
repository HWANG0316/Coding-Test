def make_dragon_curve(curve_info):
    for i in range(len(curve_info)):
        curve_dir = curve_info[i][2]             # dragon curve direction
        curve_ger = curve_info[i][3]

        if curve_dir == 0 :
            curve_list[i].append(0)
        elif curve_dir == 1: 
            curve_list[i].append(1)
        elif curve_dir == 2:
            curve_list[i].append(2)
        elif curve_dir == 3:
            curve_list[i].append(3)
        else:
            return  

        for j in range(curve_ger):

            length = len(curve_list[i])
            mid = int(length / 2)

            if j== 0 and curve_list[i][0] == 3:
                curve_list[i].append(0)
                continue
            elif j == 0:
                curve_list[i].append(curve_list[i][0] + 1)
                continue
            else:
                for k in range(0,mid):
                    number = (curve_list[i][k] + 2) %4
                    curve_list[i].append(number)

                for k in range(mid, length):
                    curve_list[i].append(curve_list[i][k])


def draw_map(curve_list, curve_info):

    for i in range(len(curve_list)):
        x = curve_info[i][0]     # start x
        y = curve_info[i][1]     # start y

        my_map[y][x] = 1

        for j in curve_list[i]:

            if j == 0 : # 동쪽
                my_map[y][x + 1] = 1
                x = x + 1 
            elif j == 1: # 북쪽
                my_map[y - 1][x] = 1
                y = y - 1
            elif j == 2: # 서쪽
                my_map[y][x - 1] = 1
                x = x -1
            elif j == 3: # 남쪽
                my_map[y + 1][x] = 1
                y = y + 1
            

def check_square(x,y):
    
    if my_map[y][x] == 1 and my_map[y][x + 1] == 1 and my_map[y + 1][x] == 1 and my_map[y + 1][x + 1] == 1:
        return True
    else:
        return False
     
def find_square():

    count = 0
    for i in range(100): # 마지막 줄은 시작점으로써 점검할 필요가 없음.
        for j in range(100):
            if check_square(j,i) == True:
                count = count + 1

    return count

my_map = [[0 for i in range(101)] for i in range(101)]  # 범위에 속은 거 같음

N = int(input())

curve_info = []
curve_list = [[] for i in range(N)]

for i in range(N):
    x, y, d, g = list(map(int, input().split()))

    if x<=100 and y<=100 and x>=0 and y>=0:
        curve_info.append([x,y,d,g])

make_dragon_curve(curve_info)    # curve make
draw_map(curve_list, curve_info)            # darw curve to map
count = find_square()
print(count)
