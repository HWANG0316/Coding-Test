key = {0:6,1:6, 2:5, 3:4, 4:3,5:2,6:1}

def solution(lottos, win_nums):
    lottos.sort()
    win_nums.sort()
    zero = lottos.count(0)

    count = 0 
    for i in lottos:
        for j in win_nums:
            if i == j:
                count = count + 1
                break
    return [key[count + zero], key[count]]