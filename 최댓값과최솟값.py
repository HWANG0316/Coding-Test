def solution(s):
    s = s.split(' ')
    max_num = max(list(map(int, s)))
    min_num = min(list(map(int, s)))
    
    max_num = str(max_num)
    min_num = str(min_num)
    
    return min_num + " " + max_num