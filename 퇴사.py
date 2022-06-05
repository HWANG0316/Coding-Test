N = int(input())

T = [0 for i in range(N)]  # 작업일 수 
P = [0 for i in range(N)]  # 이익 
dp = [0 for i in range(2*N)] # dp로 각 날의 최대 이익을 계산하기 위한 과정

for i in range(N):
    T[i], P[i] = map(int, input().split())

for i in range(N):
    if dp[i] > dp[i+1]:
        dp[i+1] = dp[i]

    if T[i] + i <= N:
        dp[i + T[i]] = max(dp[i] + P[i], dp[i + T[i]])

print(dp[N])

