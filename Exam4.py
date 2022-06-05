from itertools import permutations

def solution(s):

    result = []
    N = len(s)
    
    for i in range(N):
        for j in range(i,N):
            tmp = s[i:j + 1]
            tmp_lst = list(tmp)
            
            if tmp not in result and len(tmp)  == len(set(tmp_lst)): 
                result.append(tmp) 
    print(len(result))
    return len(result)
solution("abac")
solution("abcd")
solution("zxzxz")
