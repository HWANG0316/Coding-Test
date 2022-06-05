N, number = map(int, input().split())
result = 0

def solution(N, number):
    
    DP = [[] for i in range(10)]
    result = 0

    if N == number:
        return 1


    DP[0].append(N)

    for i in range(1,8):

        DP[i].append(DP[i-1][0] * 10 + N)         # N, NN, NNN 추가
        for j in range(i):
            for k in range(len(DP[j])):
                for l in range(len(DP[i-j-1])):
                    
                    if int(DP[j][k] + DP[i-j-1][l]) > 0 and DP[j][k] + DP[i-j-1][l] <= 32000 and DP[j][k] + DP[i-j-1][l] not in DP[i]:  # 덧셈
                        DP[i].append(DP[j][k] + DP[i-j-1][l])
                    if int(DP[j][k] - DP[i-j-1][l]) > 0 and DP[j][k] - DP[i-j-1][l] <= 32000 and DP[j][k] - DP[i-j-1][l] not in DP[i]:  # 뺄셈
                        DP[i].append(DP[j][k] - DP[i-j-1][l])
                    if int(DP[j][k] * DP[i-j-1][l]) > 0 and DP[j][k] * DP[i-j-1][l] <= 32000 and DP[j][k] * DP[i-j-1][l] not in DP[i]:  # 곱셈
                        DP[i].append(DP[j][k] * DP[i-j-1][l])
                    if int(DP[j][k] / DP[i-j-1][l]) > 0 and DP[j][k] / DP[i-j-1][l] <= 32000 and DP[j][k] / DP[i-j-1][l] not in DP[i]:  # 나눗셈
                        DP[i].append(DP[j][k] / DP[i-j-1][l])

                    if number in DP[i]:
                        return i+1
    print(DP)
    return -1


result = solution(N,number)
print(result)