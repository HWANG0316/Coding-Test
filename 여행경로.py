from collections import defaultdict

def solution(tickets):
    graph  = defaultdict(list)

    for i, j in tickets:
        graph[i].append(j)

    for i in graph.keys():
        graph[i].sort()

    print(graph)    
    stack = []
    stack.append('ICN')
    path = []
    while stack:
        v = stack.pop()

        if len(graph[v]) == 0:
            path.append(v)
        else:
            stack.append(graph[v][0])
            stack.append(graph[v].pop(0))
    print(path)
solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])