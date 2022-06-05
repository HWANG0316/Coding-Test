from itertools import combinations
groups = [[1,5],[2,7],[4,8],[3,6]]

def solution(n, groups):
    num = []
    cob = []
    answer = 0
    minnum = 10

    for i in range(len(groups)):
        num.append(i)

    
    for i in range(1, len(groups) + 1):
        cob.append(list(combinations(num,i)))

    for i in range(len(cob)):
        for j in range(len(cob[i])):
            lights = [0 for i in range(10)]
            for k in range(len(cob[i][j])):
                start = groups[cob[i][j][k]][0]
                end = groups[cob[i][j][k]][1]

                for l in range(start-1, end):
                    lights[l] = 1

                if minnum > lights.count(1):
                    minnum = lights.count(1)

                

    


    

    return answer



solution(10,groups)