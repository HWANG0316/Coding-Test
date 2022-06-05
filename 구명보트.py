from collections import deque

def solution(people, limit):
    people.sort(reverse = True)
    queue = deque(people)
    count = 0
    while len(queue) != 0:
        
        if len(queue) == 1:
            queue.pop()
            count += 1
            break

        if queue[0] + queue[-1] <=limit:
            queue.popleft()
            queue.pop()
            count += 1
        else:
            queue.popleft()
            count += 1

    return count


#print(solution([70,50,80,50], 100))
print(solution([70, 80, 50], 100))
#print(solution(	[10, 10, 10, 10, 10], 50))