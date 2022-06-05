from collections import deque   

my_queue = []
number_list = []                         # 움직인 톱니바퀴의 번호를 저장하기 위한 리스트
direction_list = []                      # 움직인 톱니바퀴의 회전 방향을 저장하기 위한 리스트

for i in range(4):                       # 각 톱니바퀴 입력
    my_queue.append(deque(map(int,input())))

time = int(input())                      # 회전 횟수 입력 

for i in range(time):                    # 움직이는 톱니바퀴 및 회전 방향 입력
    number, direction = map(int, input().split())
    number_list.append(number)
    direction_list.append(direction)
    
score_list = [1,2,4,8]

def move_check(front, back):

    if front[2] == back[6]:     # 3번 톱니와 7번 톱니가 동일할 때 움직이지 않는다.
        return True
    else:
        return False

def move_check_front(number):

    move_list = []
    for i in range(number -1, 3): # 0 1 2

        if i == (number-1):
             move_list.append(i)
        if move_check(my_queue[i], my_queue[i + 1]) == False:
            move_list.append(i)
            move_list.append(i+1)
        else:
            break

        move_list = set(move_list)
        move_list = list(move_list)
    
    return move_list

def move_check_back(number):
    move_list = []
    for i in range(number-1, 0, -1):

        if i == (number-1):
            move_list.append(i)

        if move_check(my_queue[i - 1], my_queue[i]) == False:
            move_list.append(i)
            move_list.append(i-1)
        else:
            break
        
        move_list = set(move_list)
        move_list = list(move_list)
        move_list.sort(reverse= True)
    return move_list
    
def move(direction, move_list, check = 0):
    
    if check == 1 and direction == 1:
        direction = -1
    elif check == 1 and direction == -1:
        direction = 1

    if direction == 1 : # 시계 방향
        check = 1
        for i in move_list:
            if check == 1:
                check = -1
                temp = my_queue[i].pop()
                my_queue[i].appendleft(temp)
            elif check == -1:
                check = 1
                temp = my_queue[i].popleft()
                my_queue[i].append(temp)

    elif direction == -1 : #반시계 방향
        check = -1
        for i in move_list:
            if check == -1:
                check = 1
                temp = my_queue[i].popleft()
                my_queue[i].append(temp)
            elif check == 1:
                check = -1
                temp = my_queue[i].pop()
                my_queue[i].appendleft(temp)

    

def rotate_wheel(number_list, direction_list):
    
    for i in range(len(number_list)):
        front_move_list = []
        back_move_list = []

        if number_list[i] == 1:       # 첫번째 톱니바퀴
            front_move_list = move_check_front(number_list[i])
            move(direction_list[i], front_move_list)
        elif number_list[i] == 2:
            front_move_list = move_check_front(number_list[i])
            back_move_list = move_check_back(number_list[i])
            if len(back_move_list) != 0:
                back_move_list.pop(0)
            move(direction_list[i], front_move_list)
            move(direction_list[i], back_move_list,1)
        elif number_list[i] ==3 :
            front_move_list = move_check_front(number_list[i])
            back_move_list = move_check_back(number_list[i])
            if len(back_move_list) != 0:
                back_move_list.pop(0)
            move(direction_list[i], front_move_list)
            move(direction_list[i], back_move_list, 1)


        elif number_list[i] == 4:
            back_move_list = move_check_back(number_list[i])
            move(direction_list[i], back_move_list)

        else:
            return 
def score_wheel():
    score = 0

    for i in range(4):
        if my_queue[i][0] == 0:
            continue
        else:
            score = score + score_list[i]
    return score

rotate_wheel(number_list, direction_list)

score = score_wheel()
print(score)