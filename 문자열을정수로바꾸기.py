def solution(s):
    
    lst  = list(s)
    print(lst)
    result = ""
    
    if '-' in lst:
        for i in range(1,len(lst)):
            result = result + lst[i]
        
        result = int(result) * -1
        
    else:
        
        for i in range(len(lst)):
            result = result + lst[i]
            
        result = int(result)
            
    
    return result