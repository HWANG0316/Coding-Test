def solution(m, n, puddles):
    my_map = [[0 for i in range(m)] for j in range(n)]    
    my_map[0][0] = 1

    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                continue

            if i == 0 and [j + 1,i + 1] not in puddles:
                my_map[i][j] = my_map[i][j-1]
                continue
            
            if j == 0 and [j + 1,i + 1] not in puddles:
                my_map[i][j] = my_map[i-1][j]
                continue

            if [j + 1,i + 1] not in puddles:
                my_map[i][j] = my_map[i-1][j] + my_map[i][j-1]
                continue
    print(my_map)
    return my_map[n-1][m-1] % 1000000007

solution(4,	3,	[[2, 2]])