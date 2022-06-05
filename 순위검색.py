def solution(info, query):

    lang = [[] for i in range(3)]    
    for i in range(len(info)):                      # info split
        info[i] = info[i].split(' ')

        if info[i][0] == 'cpp':
            lang[0].append(info[i])
        elif info[i][0] == 'java':
            lang[1].append(info[i])
        elif info[i][0] == 'python':
            lang[2].append(info[i])

    for i in range(len(query)):                     # query split
        query[i] = query[i].split(' and ')
        temp = query[i][3].split(' ')
        query[i][3] = temp[0]
        query[i].append(temp[1])

    count = [0 for i in range(len(query))]

    for i in query:
        if i[0] == 'cpp':
            for j in lang[0]:
                if i[:-1] == j[:-1] and j[-1] >= i[-1]:
                    count[query.index(i)] = count[query.index(i)] + 1
        elif i[0] == 'java':
            for j in lang[1]:
                if i[:-1] == j[:-1] and j[-1] >= i[-1]:
                    count[query.index(i)] = count[query.index(i)] + 1 
        elif i[0] == 'python':
            for j in lang[2]:
                if i[:-1] == j[:-1] and j[-1] >= i[-1]:
                    count[query.index(i)] = count[query.index(i)] + 1
        else:
            pass
solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])