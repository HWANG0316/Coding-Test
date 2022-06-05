def solution(msg):
    dic = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    idx = []

    while msg:
        length = len(msg)
        for i in range(length,-1, -1):
            if msg[: i] in dic:
                idx.append(dic.index(msg[:i]) + 1)

                if len(msg) != 0:
                    dic.append(msg[: i + 1])
                msg = msg[i:]
                break
    return idx
                

print(solution("KAKAO"))
print(solution("TOBEORNOTTOBEORTOBEORNOT"))
print(solution("ABABABABABABABAB"))