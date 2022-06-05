from copy import deepcopy

def solution(str1, str2):
    
    str1, str2 = str1.upper(), str2.upper()
    str1_temp, str2_temp = "", ""
    str1_lst, str2_lst = [], []

    for k in str1:
        if k >= 'A' and k <= 'Z':
            str1_temp = str1_temp + k
        else:
            str1_temp = ""

        if len(str1_temp) == 2:
            str1_lst.append(str1_temp)
            str1_temp = k

    for v in str2:
        if v >= 'A' and v <= 'Z':
            str2_temp = str2_temp + v
        else:
            str2_temp = ""

        if len(str2_temp) == 2:
            str2_lst.append(str2_temp)
            str2_temp = v

    union = list(set(str1_lst) | set(str2_lst))
    inter = list(set(str1_lst) & set(str2_lst)) 

    temp_inter = deepcopy(inter)
    for i in temp_inter:  ### 여기
        count = min(str1_lst.count(i), str2_lst.count(i))
        if count != 1:
            inter.remove(i)
            for j in range(count):
                inter.append(i)

    temp_union = deepcopy(union)
    for i in temp_union:
        count = max(str1_lst.count(i), str2_lst.count(i))
        if count != 1:
            union.remove(i)
            for j in range(count):
                union.append(i)    
    
    if len(union) == 0:
        return 65536
        
    return int((len(inter) / len(union) ) * 65536)

solution("E=M*C^2", "e=m*c^2")

