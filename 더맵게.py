import heapq

def solution(scoville, K):
    count = 0
    scoville.sort()
    while scoville[0] < K:
        
        
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        heapq.heappush(scoville, a + (b * 2))
        count = count + 1
        
        if len(scoville) <= 1:
            
            if scoville[0] < K:
                return -1
            else:
                break
    return count