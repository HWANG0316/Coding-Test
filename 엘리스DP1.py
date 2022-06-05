N = int(input())
dp = list(map(int, input().split()))
maxnum = dp[0]

for i in range(1, len(dp)):
    
    if dp[i-1] + dp[i] > 0 and dp[i-1] > 0:
        dp[i] = dp[i-1] + dp[i]

    if maxnum < dp[i]:
        maxnum = dp[i]

print(max(dp))


    



    