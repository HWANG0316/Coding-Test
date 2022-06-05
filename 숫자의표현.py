def solution(n):
    count = 0 
    for i in range(1, n // 2 + 2):
        num = 0
        for j in range(i, n //2 + 2):
            if num + j < n:
                num = num + j
            elif num + j == n:
                count = count + 1
                break
            else:
                break
    count = count + 1           # 자기 자신
    return count