global lst
lst = []

def find_road(maps,k, v, K, N, result):
    global lst
    for i in range(v + 1, N):
        if result + maps[v][i] <= K and maps[v][i] != 0:
            result = result + maps[v][i]
            lst.append(i + 1)
            find_road(maps,i,i+1, K, N, result)

def solution(N, road, K):
    global lst

    maps = [[0 for i in range(N)] for j in range(N)]
    
    for k, v, d in road:
        if maps[k-1][v-1] != 0:
            maps[k-1][v-1] = min(d, maps[k-1][v-1])
            maps[v-1][k-1] = min(d, maps[v-1][k-1])
        else:
            maps[k-1][v-1] = d
            maps[v-1][k-1] = d
        
    for i in range(1, N):
        start = maps[0][i]

        if start <= K and start != 0:
            lst.append(1)
            lst.append(i + 1)
            find_road(maps,0,i, K, N,start)

    lst = list(set(lst))
    return len(lst)

#solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3)
solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4)