dx = [1,0,-1,0]    # 상하 좌우
dy = [0,1,0,-1]

dx1 = [1,1,-1,-1]  # 대각 방향 
dy1 = [-1,1,-1,1]

def check(x, y, N, maps):
    
    for i in range(4):
        nx = x + dx[i]          # 한 칸 전진
        ny = y + dy[i]
        
        if nx >= 0 and ny >= 0 and nx < N and ny < N and maps[ny][nx] == 'P':
            return False
        
        nnx = nx + dx[i]         # 두 칸 전진
        nny = ny + dy[i]
        
        if nnx >= 0 and nny >= 0 and nnx < N and nny < N and maps[nny][nnx] == 'P':
            if maps[ny][nx] == 'O':
                return False
            
    for i in range(4):
        
        nx = x + dx1[i]
        ny = y + dy1[i]
        
        if nx >= 0 and ny >= 0 and nx < N and ny < N and maps[ny][nx] == 'P':
            if maps[ny][x] == "O" or maps[y][nx] == 'O':
                return False
            
    return True
                    
def solution(places):
    result = []
    N = len(places)
    for k in places:                # 각 대기실별로 확인
        maps = [list(v) for v in k] # 대기실 구조
        flag = 0
        for i in range(len(maps)):
            for j in range(len(maps[i])):
                if maps[i][j] == 'P':       #응시자이면 확인해야함
                    if check(j,i,N, maps) !=True:
                        flag = 1
                        break               
            if flag == 1:
                break
        if flag == 1:
            result.append(0)
        else:
            result.append(1)
            
    return result