# global max_num
# max_num = 0

# N, M = map(int, input().split())

# my_map = []

# for i in range(N):
#     my_map.append(list(map(int, input().split())))

# tetromino = [ 
#     [[0, 0], [0, 1], [0, 2], [0, 3]],  # 1  
#     [[0, 0], [1, 0], [2, 0], [3, 0]],  # 2
#     [[0, 0], [0, 1], [1, 0], [1, 1]],  # 3
#     [[0, 0], [1, 0], [2, 0], [2, 1]],  # 4
#     [[0, 0], [0, 1], [0, 2], [1, 0]],  # 5
#     [[0, 0], [0, 1], [1, 1], [2, 1]],  # 6
#     [[0, 2], [1, 0], [1, 1], [1, 2]],  # 7
#     [[0, 0], [1, 0], [1, 1], [2, 1]],  # 8
#     [[0, 1], [0, 2], [1, 0], [1, 1]],  # 9
#     [[0, 1], [1, 0], [1, 1], [1, 2]],  # 10   
#     [[0, 0], [1, 0], [2, 0], [1, 1]],  # 11
#     [[0, 0], [0, 1], [0, 2], [1, 1]],  # 12
#     [[1, 0], [0, 1], [1, 1], [2, 1]],  # 13
#     [[0, 1], [1, 1], [2, 1], [2, 0]],  # 14
#     [[0, 0], [0, 1], [0, 2], [1, 2]],  # 15
#     [[0, 0], [0, 1], [1, 0], [2, 0]],  # 16
#     [[0, 0], [1, 0], [1, 1], [1, 2]],  # 17
#     [[0, 1], [1, 0], [1, 1], [2, 0]],  # 18
#     [[0, 0], [0, 1], [1, 1], [1, 2]]   # 19 # check check check 
# ]

# def move(x, y, num):      # move tetromino
#     global max_num    
#     tet = tetromino[num]

#     first_x = tetromino[num][0][0] + x
#     first_y = tetromino[num][0][1] + y

#     second_x = tetromino[num][1][0] + x
#     second_y = tetromino[num][1][1] + y

#     third_x = tetromino[num][2][0] + x
#     third_y = tetromino[num][2][1] + y

#     fourth_x = tetromino[num][3][0] + x 
#     fourth_y = tetromino[num][3][1] + y

#     if first_x >= 0 and first_y >= 0 and second_x >= 0 and second_y >= 0 and third_x >= 0 and third_y >= 0 and fourth_x >= 0 and fourth_y >= 0 and first_x < M and second_x < M and third_x < M and fourth_x < M and first_y < N and second_y < N and third_y < N and fourth_y < N: 
#         result_sum = 0
#         result_sum = result_sum + my_map[first_y][first_x] + my_map[second_y][second_x] + my_map[third_y][third_x] + my_map[fourth_y][fourth_x] 

#         if max_num < result_sum:
#             max_num = result_sum

# for i in range(19):    # tetromino for 
#     for j in range(N):   # 밑으로   y
#         for k in range(M):   # 옆으로  x
#             move(k, j, i)


# print(max_num)



N,M=map(int,input().split())
board=[]
board=[[int(i) for i in input().split()]for j in range(N)]
global result
result=0

def woo(x,y):
    global result

    sum=0
    if x>=0 and x+1<N and y>=0 and y+2<M:   #ㅜ
        sum=board[x][y]+board[x][y+1]+board[x][y+2]+board[x+1][y+1]
        result=max(sum,result)
    elif x>=0 and x+2<N and y>=0 and y+1<M: #ㅏ
        sum=board[x][y]+board[x+1][y]+board[x+2][y]+board[x+1][y+1]
        result=max(sum,result)
    elif x>=1 and x+1<N and y>=0 and y+1<M: #ㅓ
        sum=board[x][y]+board[x][y+1]+board[x-1][y+1]+board[x+1][y+1]
        result=max(sum,result)
    elif x>=0 and x+1<N and y>=1 and y+1<N: #ㅗ
        sum=board[x][y]+board[x+1][y]+board[x+1][y+1]+board[x+1][y-1]
        result=max(sum,result)
        
        
def l(x,y):
    global result

    sum=0
    if x>=0 and x+3<N and y>=0 and y<M: #l
        sum=board[x][y]+board[x+1][y]+board[x+2][y]+board[x+3][y]
        result=max(sum,result)
    elif x>=0 and x<N and y>=0 and y+3<M: #l
        sum=board[x][y]+board[x][y+1]+board[x][y+2]+board[x][y+3]
        result=max(sum,result)

def m(x,y):
    global result

    sum=0
    if x>=0 and x+1<N and y>=0 and y+1<M:
        sum=board[x][y]+board[x+1][y]+board[x][y+1]+board[x+1][y+1]
        result=max(result,sum)
        
def L(x,y):
    global result

    sum=0
    if x>=0 and x+2<N and y>=0 and y+1<M:
        sum=board[x][y]+board[x+1][y]+board[x+2][y]+board[x+1][y+1]
        result=max(result,sum)
    elif x>=0 and x+1<N and y>=0 and y+2<M:
        sum=board[x][y]+board[x+1][y]+board[x][y+1]+board[x][y+2]
        result=max(result,sum)
    elif x>=0 and x+2<N and y>=0 and y+1<M:
        sum=board[x][y]+board[x][y+1]+board[x+1][y+1]+board[x+2][y+1]
        result=max(result,sum)
    elif x>=0 and x+1<N and y<M and y-2>=0:
        sum=board[x][y]+board[x+1][y]+board[x+1][y-1]+board[x+1][y-2]
        result=max(result,sum)
    elif x>=0 and x+2<N and y>=0 and y+1<M:
        sum=board[x][y]+board[x+1][y]+board[x+2][y]+board[x][y+1]
        result=max(result,sum)
    elif x>=0 and x+1<N and y>=0 and y+2<M:
        sum=board[x][y]+board[x+1][y]+board[x+1][y+1]+board[x+1][y+2]
        result=max(result,sum)
    elif x>=0 and x+2<N and y<M and y-1>=0:
        sum=board[x][y]+board[x+1][y]+board[x+2][y]+board[x+2][y-1]
        result=max(result,sum)       
    elif x>=0 and x+1<N and y>=0 and y+2<M:
        sum=board[x][y]+board[x][y+1]+board[x][y+2]+board[x+1][y+2]
        result=max(result,sum)
def z(x,y):
    global result

    sum=0
    if x>=0 and x+2<N and y>=0 and y+1<M:
        sum=board[x][y]+board[x+1][y]+board[x+1][y+1]+board[x+1][y+1]
        result=max(result,sum)
    elif x<N and x-1>=0 and y>=0 and y+2<M:
        sum=board[x][y]+board[x][y+1]+board[x-1][y+1]+board[x-1][y+2]
        result=max(sum,result)
    elif x>=0 and x+2<N and y<M and y-1>=0:
        sum=board[x][y]+board[x+1][y]+board[x+1][y-1]+board[x+2][y-1]
        result=max(result,sum)
    elif x>=0 and x+1<N and y>=0 and y+2<M:
        sum=board[x][y]+board[x][y+1]+board[x+1][y+1]+board[x+1][y+2]
        result=max(result,sum)        

for i in range(N):
    for j in range(M):
        woo(i,j)
        l(i,j)
        m(i,j)
        L(i,j)
        z(i,j)
print(result)

