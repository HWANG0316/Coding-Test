N, number = map(int, input().split())
result = 0

def solution(N, number):
    
    DP = [[] for i in range(10)]
    result = 0

    if N == number:
        return 1

    for i in range(9):
        if i == 0 :
            DP[i].append(N)
            continue

        for j in range(pow(2,2*i -2) + 1):
            
            if i == 1:
                DP[i].append(DP[i-1][0] * 10 + N)
                DP[i].append(DP[i-1][j] + N)
                DP[i].append(DP[i-1][j] - N)
                DP[i].append(DP[i-1][j] * N)
                DP[i].append(DP[i-1][j] / N)

                if number in DP[i]:
                    result = i + 1
                    return result
                break

            if len(DP[i]) == 0:
                DP[i].append(DP[i-1][0] * 10 + N)
            DP[i].append(int(DP[i-1][j] + N))
            DP[i].append(int(DP[i-1][j] - N))
            DP[i].append(int(DP[i-1][j] * N))
            DP[i].append(int(DP[i-1][j] / N))
        
            if number in DP[i]:
                result = i + 1
                return result
        
        print(DP[i])
    return -1


result = solution(N,number)
print(result)