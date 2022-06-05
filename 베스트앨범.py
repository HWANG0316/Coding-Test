def solution(genres, plays):
    c_dict = {}                                 # 장르별 총 재생 횟수
    g_dict = {}                                 # 장르 몇 index, 횟수 담음
    genre = []                                  # 장르 종류만 담음
    for i in range(len(genres)):
        if genres[i] not in c_dict.keys():
            c_dict[genres[i]] = plays[i]
            g_dict[genres[i]] = [[i, plays[i]]]
            genre.append(genres[i])
        else:
            c_dict[genres[i]] = c_dict[genres[i]] + plays[i]
            g_dict[genres[i]] = g_dict[genres[i]] + [[i,plays[i]]]

    for i in genre:
        g_dict[i].sort(key = lambda x:(-x[1], x[0]))         # 장르 내에서 많이 재생된 노래 수록  하면 할수록 늘어나는 코딩 실력
        g_dict[i] = g_dict[i] + [c_dict[i]]

    sorted_c_dict = sorted(c_dict.items(), key = lambda x:x[1], reverse= True)
    result  = []

    for i in range(len(sorted_c_dict)):
        if len(g_dict[sorted_c_dict[i][0]]) == 2:
            result.append(g_dict[sorted_c_dict[i][0]][0][0])
        else:
            result.append(g_dict[sorted_c_dict[i][0]][0][0])
            result.append(g_dict[sorted_c_dict[i][0]][1][0]) 

    print(result)
    return result

#solution(["classic", "pop", "classic", "classic", "pop"] ,[500, 600, 500, 800, 2500])
solution(["A", "A", "B", "A", "B", "B", "A", "A", "A", "A"], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])