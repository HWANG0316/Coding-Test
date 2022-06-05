import math

def solution(n,a,b):
    number = [a-1,b-1]  ## 리스트에서의 인덱스
    number.sort()
    
    while n != 1:
        n = n / 2
        if number[0] <n and number[1] >= n:
            return math.log2(n*2)
        elif number[0] >=n and number[1] >= n:
            number[0] = number[0] - n
            number[1] = number[1] - n