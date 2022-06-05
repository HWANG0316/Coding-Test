def solution(n):
    result = ""
    
    for i in range(n):
        if i % 2 == 0:
            result = result + "수"
        else:
            result = result + "박"
            
    return result