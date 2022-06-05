def solution(answers):
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    
    count_a = 0
    count_b = 0
    count_c = 0
    for i in range(len(answers)):
        
        if a[i % 5] == answers[i]:
            count_a = count_a + 1
        
        if b[i % 8] == answers[i]:
            count_b = count_b + 1
        
        if c[i % 10] == answers[i]:
            count_c = count_c + 1
            
        
    result = [count_a, count_b, count_c]
    
    print(result)
    
    if result.count(max(result)) == 3:
        return [1,2,3]
    elif result.count(max(result)) == 2:
        first = result.index(max(result)) + 1
        result[first - 1] = result[first - 1] - 1
        second = result.index(max(result)) + 1
        
        return [first,second]
    else:
        return [result.index(max(result)) + 1]