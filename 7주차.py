def solution(enter, leave):
    temp, count, number = [], [0 for i in range(len(enter))], len(enter)
    e_idx, l_idx = 0, 0
    
    while e_idx < number or l_idx < number:
        
        fo_count = len(temp)
        for i in range(fo_count):
            if leave[l_idx] in temp and l_idx < number:
                temp.pop(temp.index(leave[l_idx]))
                l_idx = l_idx + 1
        

        if e_idx < number:
            temp.append(enter[e_idx])
            e_idx = e_idx + 1

        if len(temp) > 1:
            count[enter[e_idx - 1] - 1] = len(temp) - 2
            for i in temp:
                count[i - 1] = count[i-1] + 1
        
        

    print(count)
#solution([1,3,2],[1,2,3])
#solution([1,4,2,3],[2,1,3,4])
solution([1,4,2,3],[2,1,4,3])

