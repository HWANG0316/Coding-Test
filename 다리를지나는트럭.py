from collections import deque

def solution(bridge_length, weight, truck_weights):
    
    queue = deque(maxlen = bridge_length)
    
    current_weight = 0
    time = 0
    num = 0
    while 1:
        
        if num == len(truck_weights) and sum(queue) == 0:
            break

        if len(queue) == bridge_length:
            current_weight -= queue.pop()
             
        if num == len(truck_weights):
            queue.appendleft(0)
        elif current_weight + truck_weights[num] <= weight:
            queue.appendleft(truck_weights[num])
            current_weight += truck_weights[num]
            num += 1
        else:
            queue.appendleft(0)
        time += 1
    return time



print(solution(2,10,[7,4,5,6]))
#print(solution(100, 100, [10]))
#print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
    
    
    