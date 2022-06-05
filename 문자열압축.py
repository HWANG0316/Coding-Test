def solution(s):
    
    if len(s) == 1:
        return 1
    l = len(s)
    result_lst = []
    for i in range(1,l //2 + 1):      # 문자 단위 
        
        key = s[:i]
        count = 1
        result = ""
        for j in range(i,l,i):   # 옆으로 이동하면서 비교
            if key == s[j:j+i] :
                count = count + 1
            else:
                if count == 1:
                    result = result + key
                else:
                    result = result + str(count) + key
                key = s[j:j+i]
                count = 1
                
            if j + i >= l:
                if count == 1:
                    result = result + key
                else:
                    result = result + str(count) + key
        result_lst.append(len(result))
    
    return min(result_lst)