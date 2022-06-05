def solution(arr):
    result = 0
    count = 1
    
    while(1):
        
        for i in range(len(arr) - 1):
            
            if (arr[len(arr) - 1] * count) % arr[i] == 0:
                if i == (len(arr) - 2):
                    return arr[len(arr) - 1] * count
                else:
                    continue
            else:
                count = count + 1
                break