def check(num):
    count = 0
    for i in range(1,num + 1):
        if num % i == 0:
            count = count + 1
    if count % 2 == 0:
        return True
    else:
        return False
def solution(left, right):
    
    result = 0
    for i in range(left, right +1):
        if check(i) == True:
            result += i
        else:
            result -= i
    return result