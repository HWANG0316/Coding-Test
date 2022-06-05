def solution(board):
    dp = [[0 for i in range(len(board[0]))] for j in range(len(board))]

    dp[0] = board[0]
    max_num = max(board[0])
    for i in range(1, len(board)):
        dp[i][0] = board[i][0]
    
    for i in range(1, len(board)):
        for j in range(1, len(board[i])):
            if board[i][j] == 0:
                dp[i][j] = 0
                continue

            if dp[i][j-1] == dp[i-1][j] and dp[i-1][j] == dp[i-1][j-1]:
                dp[i][j] = dp[i][j-1] + 1

                if max_num < dp[i][j]:
                    max_num = dp[i][j]
            else: 
                if min(dp[i][j-1],dp[i-1][j], dp[i-1][j-1]) == 0:
                    dp[i][j] = board[i][j]
                    if max_num < dp[i][j]:
                        max_num = dp[i][j]
                else:
                    dp[i][j] = min(dp[i][j-1],dp[i-1][j], dp[i-1][j-1]) + 1
                    if max_num < dp[i][j]:
                        max_num = dp[i][j]
    return max_num * max_num
#print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))
#solution([[0,0,1,1],[1,1,1,1]])
#print(solution(	[[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
print(solution(	[[0, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0]]))