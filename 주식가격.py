from copy import deepcopy

def solution(prices):
    result = []
    N = len(prices)
    for i in range(N):
        num = prices[i]
        for j in range(i, N):
            if prices[j] - num < 0:
                result.append(j - i)
                break

            if j == N -1:
                result.append(j-i)
    return result