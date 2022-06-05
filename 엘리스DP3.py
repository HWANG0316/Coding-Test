N = int(input())
dp = [[0 for i in range(100)] for i in range(9)]

dp[0][0] = 1
for i in range(1,9):
    dp[i][0] = dp[i-1][0] + 1

for i in range(1,N):
    for j in range(9):
        if j == 0:
            dp[0][i] = 1 
        else:
            dp[j][i] = dp[j][i-1] + dp[j-1][i-1]

result = dp[8][N-1] % 1000000000

print(result)

import heapq
