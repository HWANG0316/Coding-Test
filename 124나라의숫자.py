def solution(n):
    
    rev_base = ''
    
    while n > 0:
        n, mod = divmod(n-1, 3)
        rev_base += str(mod)
        
    rev_base = rev_base[::-1]
    
    result = ""
    for i in rev_base:
        if i == '0':
            result = result + '1'
        elif i == '1':
            result = result + '2'
        elif i == '2':
            result = result + '4'
    
    return result