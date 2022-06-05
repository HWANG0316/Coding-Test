def solution(array, commands):
    
    result = []
    for i in range(len(commands)):
        temp = array[commands[i][0] - 1 : commands[i][1]]
        temp.sort()
        result.append(temp[commands[i][2] - 1])

    return result