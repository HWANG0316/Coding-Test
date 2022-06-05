from itertools import combinations

N, M = map(int, input().split())

my_map = []
chick_list = []
house_list = []
dist = 0

for i in range(N):
    my_map.append(list(map(int, input().split())))

def find_chicken():
    chick_list = []

    for i in range(N):
        for j in range(N):
            if my_map[i][j] == 2:
                chick_list.append([i,j])
    return chick_list

def find_house():
    house_list = []

    for i in range(N):
        for j in range(N):
            if my_map[i][j] == 1:
                house_list.append([i, j])
    return house_list
 
def find_min_dist(chick_list, house_list):
    comb = []
    sum_list = []
    dist = 0

    for i in range(1, M + 1):
        comb =list(combinations(chick_list,i))

        for k in range(len(comb)):          # 각각의 comb에 대해서
            min_list = [] 
            for j in range(len(house_list)):  # 각 집에 대해서 
                min_dist = 1000000
                result = 0

                for l in range(len(comb[0])):  #  각 치킨집에 대해서
                    result = abs(house_list[j][0] - comb[k][l][0]) + abs(house_list[j][1] - comb[k][l][1])

                    if result < min_dist:
                        min_dist = result
            
                min_list.append(min_dist)

            sum_list.append(sum(min_list))

    dist = min(sum_list)
    return dist
    
chick_list = find_chicken()
house_list = find_house()
dist = find_min_dist(chick_list, house_list)

print(dist)