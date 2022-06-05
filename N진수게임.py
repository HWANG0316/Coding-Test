def solution(n, t, m, p):
    num_A = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    candi = "0"
    for i in range(1,t*m):          # 수 구하기
        num = ""
        while i > 0:
            i , mod = divmod(i,n)
            mod = num_A[mod]
            num = num + mod
        candi = candi + num[::-1]

    result = ""

    for i in range(t*m):
        if (i % m) + 1 == p:
            result = result + candi[i]
    return result
#solution(2, 4, 2, 1)
solution(16, 16, 2,	1)
#solution(16, 16, 2, 2)

# n: 진법 
# t: 미리 구할 수 개수
# m: 참여 인원
# p: 튜브 순서
