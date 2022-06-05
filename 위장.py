def solution(clothes):
    cloth = {}
    result = 1
    
    for i in clothes:
        if i[1] not in cloth.keys():
            cloth[i[1]] = 1
        else:
            cloth[i[1]] = cloth[i[1]]+ 1
    
    for i in cloth.values():
        result = result * (i + 1)
    result = result - 1
    return result
solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]])