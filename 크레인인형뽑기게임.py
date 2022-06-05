def solution(board, moves):
    
    result = []
    count = 0
    print(moves)
    for i in moves:
        temp = 0
        for j in range(len(board)):
            if board[j][i-1] != 0:
                result.append(board[j][i-1])
                temp = board[j][i-1]
                board[j][i-1] = 0
                 
                if len(result) > 1:
                    if  result[len(result)-1] == result[len(result) -2]:
                        result.pop()
                        result.pop()
                        count = count + 2
                
                break
            
            
            
    return count