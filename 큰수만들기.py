from itertools import combinations
from copy import deepcopy

def solution(number, k):
    
    idx_list = list(number)
    comb = list(combinations(idx_list, k))
    result = []
    
    for i in comb:
        temp = deepcopy(idx_list)
        for j in i:
            temp.remove(j)
        result.append(''.join(temp))
        
    return max(result)

    ## 시간 초과 ##