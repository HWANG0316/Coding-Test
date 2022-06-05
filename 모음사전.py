global count
global dic

count = 0
dic = []
alpha = ['A', 'E','I','O','U']

def dfs(n_alpha, word):
    if len(n_alpha) <5:
        for i in range(5):
            nx_alpha = n_alpha + alpha[i] 
            
            if len(nx_alpha) <= 5:
                dic.append(nx_alpha)
                dfs(nx_alpha, word)
            else:
                break
                
def solution(word):
    for i in range(5):
        dic.append(alpha[i])
        dfs(alpha[i], word)

    print(dic.index(word) + 1)

solution("AAAAE")
solution("AAAE")
solution("I")
solution("EIO")