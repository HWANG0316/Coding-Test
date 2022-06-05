def solution(s):
    
    temp = list(s)
    
    if len(temp) != 4 and len(temp) != 6:
        return False
    
    for i in range(len(temp)):
        
        if (ord(temp[i]) >=65 and ord(temp[i]) <=90) or (ord(temp[i]) >=97 and ord(temp[i]) <= 122):
            return False
        
    
    return True