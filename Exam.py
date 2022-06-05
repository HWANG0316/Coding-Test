# 접속자가 많을 때에는 서버 많이, 적을 때에는 적게 띄우자.
# 각 시간대에 발생한 로그 수를 파악해 미래에 서버 몇대 띄울지 계산

def solution(friends, user_id):

    name_lst = []
    friends_lst = []
    for k, v in friends:

        if k not in name_lst:
            friends_lst.append([v])
            name_lst.append(k)
        else:
            friends_lst[name_lst.index(k)].append(v)


        if v not in name_lst:
            friends_lst.append([k])
            name_lst.append(v)
        else:
            friends_lst[name_lst.index(v)].append(k)    


    print(name_lst)
    print(friends_lst)
    f_count = [0 for i in range(len(name_lst))]
    idx = name_lst.index(user_id)  ## 0 이 나옴

    for i in friends_lst[idx]:
        f_idx = name_lst.index(i)

        for j in friends_lst[f_idx]:
            f_count[name_lst.index(j)] = f_count[name_lst.index(j)] + 1 

    f_count[name_lst.index(user_id)] = 0
    print(f_count)

    max_count = max(f_count)
    result_lst = []
    for i in range(len(f_count)):
        if f_count[i] == max_count:
            result_lst.append(name_lst[i])

    print(result_lst)

solution([["david", "frank",], ["demi", "david"], ["frank", "james"], ["demi", "james"], ["claire", "frank"]], "david")