def solution(priorities, location):
    
    N = len(priorities)
    check = 0
    while check != 1:
        ready = priorities.pop(0)
        
        if len(priorities) != 0:
            if ready >= max(priorities): 
                if location == 0:
                    return N- len(priorities)
                else:
                    location = location - 1         # PRINT
            else:
                if location == 0:
                    priorities.append(ready)
                    location = len(priorities) - 1
                else:
                    priorities.append(ready)
                    location = location - 1
        else:
            return N