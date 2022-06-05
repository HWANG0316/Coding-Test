def solution(operations):
    
    queue = []
    
    for i in operations:
        k, num = i.split()
        
        if k == 'I':
            queue.append(int(num))
        elif k == 'D' and num == '1':
            queue.sort()
            queue.pop()
        elif k == 'D' and num == "-1":
            queue.sort()
            queue.pop(0)

    if len(queue) == 0:
        return [0,0]
    else:
        return [max(queue), min(queue)]
#solution(["I 16","D 1"])
solution(["I 7","I 5","I -5","D 1"]	)
    