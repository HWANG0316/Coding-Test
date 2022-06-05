def solution(arr1, arr2):
    rmtrx = [[0 for i in range(len(arr2[0]))] for j in range(len(arr1))]
    
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for k in range(len(arr1[0])):
                
                rmtrx[i][j] = rmtrx[i][j] + arr1[i][k] * arr2[k][j]
                
                
    
    return rmtrx