def solution(n, arr1, arr2):
    
    map1 = []
    map2 = []
    result_map = []
    for i in range(n):
        map1 = list(format(arr1[i], '0' + str(n) + 'b'))
        map2 = list(format(arr2[i], '0' + str(n) + 'b'))
        
        temp = []
        for j in range(n):    
            if map1[j] == map2[j]:
                temp.append(map1[j])
            elif map1[j] > map2[j]:
                temp.append(map1[j])
            elif map1[j] < map2[j]:
                temp.append(map2[j])
            
        result_map.append(temp)
            
    for i in range(n):
        for j in range(n):
            if result_map[i][j] == '1':
                result_map[i][j] = '#'
            else:
                result_map[i][j] = ' '
                
    for i in range(n):
        result_map[i] = ''.join(result_map[i])
        
    return result_map