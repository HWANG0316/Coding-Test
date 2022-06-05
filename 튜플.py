def solution(s):
    s = s[1:-1]
    s_lst, temp, result = [], [], []
    string = ""
    for i in s:
        if i == "{":
            continue
        elif i == "}":
            temp.append(int(string))
            string = ""
            s_lst.append(temp)
            temp = []
        elif i == "," and len(string) != 0:
            temp.append(int(string))
            string = ""
        elif i != "," and i != '{' and i !='}':
            string = string + i 
                    
    s_lst = sorted(s_lst, key = len)
    
    result.append(s_lst[0][0])
    for i in range(1,len(s_lst)):
        result.append(list(set(s_lst[i]) -set(s_lst[i-1]))[0])
    print(result)
    return result