N, M, y, x , K  = map(int, input().split())

my_map = [[0 for i in range(M)] for i in range(N)]

for i in range(N):
    my_map[i] = list(map(int,input().split()))


order = list(map(int,input().split()))     # 명령 입력

real_order = []                            # map을 벗어나지 않는 명령들을 선별하여 저장하기 위한 리스트

for i in range(len(order)):                # map을 벗어나지 않는 명령 선별 

    if i == 0:
        current_x = x
        current_y = y

    if order[i] == 1:     # 동쪽
        if M > (current_x + 1) and (current_x + 1) >= 0:
            real_order.append(order[i])
            current_x = current_x + 1

    elif order[i] == 2:   # 서쪽
        if M > (current_x - 1) and (current_x - 1) >= 0:
            real_order.append(order[i])
            current_x = current_x - 1

    elif order[i] == 3:   # 북쪽
        if N > (current_y - 1) and (current_y - 1) >= 0:
            real_order.append(order[i])
            current_y = current_y - 1

    elif order[i] == 4:   # 남쪽
        if N > (current_y + 1) and (current_y + 1) >= 0 :
            real_order.append(order[i])
            current_y = current_y + 1


front, back, right, left, top, bottom = 0, 0, 0, 0, 0, 0

for i in range(len(real_order)):

    if i == 0:
        current_x = x
        current_y = y
    

    if real_order[i] == 1:                              # 동쪽
        current_x = current_x + 1
        
        temp = bottom
        bottom = right
        right = top
        top = left
        left = temp
        
        if my_map[current_y][current_x] == 0:
            my_map[current_y][current_x] = bottom
        else:
            bottom = my_map[current_y][current_x]
            my_map[current_y][current_x] = 0


        print(top)

    elif real_order[i] == 2:                            # 서쪽
        current_x = current_x - 1
        
        temp = bottom
        bottom = left
        left = top
        top = right
        right = temp

        if my_map[current_y][current_x] == 0:
            my_map[current_y][current_x] = bottom
        else:
            bottom = my_map[current_y][current_x]
            my_map[current_y][current_x] = 0

        print(top)

    elif real_order[i] == 3:                            # 북쪽
        current_y = current_y - 1
        
        temp = bottom
        bottom = front
        front = top
        top = back
        back = temp

        if my_map[current_y][current_x] == 0:
            my_map[current_y][current_x] = bottom
        else:
            bottom = my_map[current_y][current_x]
            my_map[current_y][current_x] = 0

        print(top)

    elif real_order[i] == 4:                            # 남쪽
        current_y = current_y + 1
        
        temp = bottom
        bottom = back
        back = top
        top = front
        front = temp 

        if my_map[current_y][current_x] == 0:
            my_map[current_y][current_x] = bottom
        else:
            bottom = my_map[current_y][current_x]
            my_map[current_y][current_x] = 0
        
        print(top)
    
