from itertools import permutations
from itertools import combinations

N = int(input())

my_map = []
member = []   # 게임할 멤버들

for i in range(N):
    my_map.append(list(map(int, input().split())))   # input
    member.append(i)                             # append member

def diff_score():  # 팀 간 점수차이를 구함.
    pass

def cal_team_score(start_team, link_team): # 팀 점수를 계산
    
    permu_start = list(permutations(start_team, 2))  # 각 팀의 순서쌍을 구하기 위한 순열
    permu_link =  list(permutations(link_team, 2))
  
    start_team_score = 0
    link_team_score = 0
    diff = 0 

    for i in range(len(permu_start)):
        start_team_score = start_team_score + my_map[permu_start[i][0]][permu_start[i][1]]
        link_team_score = link_team_score + my_map[permu_link[i][0]][permu_link[i][1]] 

    diff = abs(start_team_score - link_team_score)

    return diff

def make_team():    # 팀을 만듬
    comb = list(combinations(member, N//2))    # 주어진 인원을 조합을 통해 반씩 나눔. 이때 앞뒤로 쌍이 적절하게 맞다.        
    start_team = comb[:len(comb)//2]           # start team candi
    link_team = comb[len(comb)//2:]            #  link team candi
    link_team.reverse()
    
    diff_list = []

    for i in range(len(start_team)):
        diff = cal_team_score(start_team[i], link_team[i])
        diff_list.append(diff)

    print(min(diff_list))


make_team()
