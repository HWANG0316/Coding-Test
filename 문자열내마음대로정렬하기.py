def solution(strings, n):
    lst = []
    
    for i in range(len(strings)):
        lst.append([strings[i][n], strings[i]])
        
    lst.sort()
    
    result = []
    for i in range(len(lst)):
        result.append(lst[i][1])
        
    print(result)
    
    return result