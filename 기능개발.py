def solution(progresses, speeds):
    
    result = []
    for k in range(100):            # 많이 해봤자 100일 일함.
        print(progresses)
        count = 0
        for i in range(len(progresses)):                # 하루 작업 추가
            progresses[i] = progresses[i] + speeds[i]

        
        for i in range(len(progresses)):                # 하루하루 체크
            if progresses[i] >= 100:
                count = count + 1
            else:
                break
    
        if count != 0:
            progresses = progresses[count:]
            speeds = speeds[count:]
            result.append(count)
            
        if len(progresses) == 0:
            break      
    return result