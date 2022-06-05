def solution(land):
    temp = [[0 for i in range(4)] for j in range(len(land))]
    temp[0] = land[0]
    
    for i in range(1,len(land)):
        for j in range(4):
            if j == 0:
                temp[i][j] = max(land[i][j] +temp[i-1][1],land[i][j] +temp[i-1][2],land[i][j] +temp[i-1][3])
            elif j == 1:
                temp[i][j] = max(land[i][j] +temp[i-1][0],land[i][j] +temp[i-1][2],land[i][j] +temp[i-1][3])
            elif j == 2:
                temp[i][j] = max(land[i][j] +temp[i-1][0],land[i][j] +temp[i-1][1],land[i][j] +temp[i-1][3])
            elif j == 3:
                temp[i][j] = max(land[i][j] +temp[i-1][0],land[i][j] +temp[i-1][1],land[i][j] +temp[i-1][2])
    
    return max(temp[-1])