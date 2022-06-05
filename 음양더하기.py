def solution(absolutes, signs):
    
    result = 0
    for i in range(len(absolutes)):
        
        if signs[i] == True:
            result = result + absolutes[i]
        else:
            result = result - absolutes[i]
    return result