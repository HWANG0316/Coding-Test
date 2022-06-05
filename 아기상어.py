# 가장 가까운 물고기를 먹으러 감.
# 위, 왼쪽 물고기를 우선적으로 먹음.
# 자신의 크기보다 작으면 먹을 수 있고, 크기가 같다면 지나갈 수 있다.
# 아기 상어는 자신의 크기와 같은 수의 물고기를 먹을 때마다 크키가 1 증가함.
# 아기 상어가 도움을 요청하지 않고 물고기를 잡아먹을 수 있는 시간을 출력함.


my_map = []        # graph
visited = []       

dx = [0, -1, 1, 0] # 위 왼쪽 오른쪽 아래
dy = [-1, 0, 0, 1]


def dfs(x, y):

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < N and ny >= 0 and ny < N and visited[ny][nx] != 1:
            pass

N = int(input())

for i in range(N):
    my_map.append(list(map(int, input().split())))




