def isCorrect(p):                             # 조건 3
    if p.count('(') == p.count(')'):
        temp = []
        for i in p:
            if len(temp) == 0 and i == ')':
                return False

            if i == ')':
                temp.pop()
            else:   
                temp.append(i)
        return True
def one_three(p):
    if p == "":
        return ""

    result = ""
    for i in range(len(p) + 1):
        first = p[:i]
        second = p[i:]

        if first.count('(') == first.count(')') and second.count('(') == second.count(')') and len(first) != 0:
            u, v = first, second
            break

    if isCorrect(u) == True:
        p = one_three(v)
        result = u +  result + p
        return result
    else:
        p = one_three(v)
        temp = "("
        temp = temp + p + ")"
        u = u[1:-1]

        temp_str = ""
        for i in range(len(u)):
            if u[i] == '(':
                temp_str = temp_str + ')'
            else:
                temp_str = temp_str + '('
        temp = temp + temp_str

        return temp
    


def solution(p):
    if isCorrect(p) == True:
        return p

    p = one_three(p)
    return p
print(solution("(()())()"))
#print(solution(	")("))
#print(solution("()))((()"))

    
    