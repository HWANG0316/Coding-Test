from collections import deque

def solution(numbers, target):
    
    num = []
    num.append(0)

    while numbers:
        temp = []
        for i in num:
            plus = i + numbers[0]
            minus = i - numbers[0]
            temp.append(plus)
            temp.append(minus)
        numbers.pop(0)
        num = temp
    
    count = 0
    for i in num:
        if i == target:
            count = count + 1
    return count