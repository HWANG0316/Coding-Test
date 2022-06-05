k = int(input())
coin = [1, 2, 5, 10, 20, 50, 100, 200]

dp = [0 for i in range(3000)]

dp[0] = 1


for i in range(len(coin)):
    for j in range(0, k+1):

        if((j- coin[i]) >= 0):
            dp[j] = dp[j] + dp[j-coin[i]]



print(dp[k])