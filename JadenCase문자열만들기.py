def solution(s):
    
    s_list = s.split(' ')
    n_list = []
    
    for i in range(len(s_list)):
        new_str = ""
        for j in range(len(s_list[i])):
            if j == 0 and s_list[i][j].islower() == True:
                    new_str = new_str + s_list[i][j].upper()
            elif j != 0 and s_list[i][j].isupper() == True:
                    new_str = new_str + s_list[i][j].lower()
            else:
                new_str = new_str + s_list[i][j]
        n_list.append(new_str)

    n_str = n_list[0]
    for i in range(1, len(n_list)):
        n_str = n_str + " " + n_list[i]
                                     
    return n_str