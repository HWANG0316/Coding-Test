from collections import deque
from collections import defaultdict
def solution(begin, target, words):
    
    def counting_diff(graph, k, words):
        for i in words:
            count = 0
            
            if i == k:
                continue
            
            for j in range(len(k)):

                if k[j] != i[j]:
                    count += 1              # 1개만 다른 경우
            if count == 1:
                graph[k].append(i)

    words.append(begin)
    graph = defaultdict(list)
    visited = {}
    
    for i in words:
        counting_diff(graph, i, words)
        visited[i] = False

    queue = deque()
    queue.append((begin, 0))
    visited[begin] = True 

    count = 0
    while queue:
        v, depth = queue.popleft()
        for i in graph[v]:
            if visited[i] != True:

                if i == target:
                    print(depth + 1)
                    return depth + 1
                visited[i] = True
                queue.append((i,depth +1))
    return 0

                
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]), 4)
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]), 0)