def solution(s):
    """
    while "()" in s:
        if s[0] == ")" or s[-1] == "(":
            return False
        s = s.replace("()","")
    return True if s == "" else False
    """             # replace의 복잡도가 생각보다 큰 듯하다. O(N*N)이 되는 경우도
                    # 존재한다고 함.
        
    lst = []
    for i in s:
        if i == "(":
            lst.append(i)
        else:
            if len(lst) == 0:
                return False

            if lst.pop() !="(":
                return False
    if len(lst) == 0:
        return True
    else:
        return False