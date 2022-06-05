def solution(n):
    one_count = bin(n).count('1')
    
    for i in range(n + 1, 1000000):
        
        if bin(i).count('1') == one_count:
            return i