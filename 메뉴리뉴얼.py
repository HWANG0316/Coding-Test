from itertools import combinations
from copy import deepcopy

def solution(orders, course):
    k = [sorted(list(a)) for a in orders]
    result = []
    for j in course:
        comb = [list(combinations(i,j)) for i in k]

        extend_comb = []
        for v in comb:
            extend_comb.extend(v)
        set_comb = sorted(set(extend_comb))
        
        max_count = 2
        max_comb_idx = []
        for v in set_comb:
            if extend_comb.count(v) > max_count:
                max_count = extend_comb.count(v)
                max_comb_idx = []
                max_comb_idx.append(v)
            elif extend_comb.count(v) == max_count:
                max_comb_idx.append(v)
        
        for v in range(len(max_comb_idx)):
            max_comb_idx[v] = list(max_comb_idx[v])
        
        if len(max_comb_idx) == 0:
            continue
        else:
            for v in range(len(max_comb_idx)):
                result.append(''.join(max_comb_idx[v]))
        
    result.sort()
    return result