
def solution(bridge_length, weight, truck_weights):
    dp = [0 for i in range(bridge_length)]
    num, time = 0, 0                                         # 이번에 건너야 할 트럭 순서 
    while 1:
        
        if num == len(truck_weights):
            for i in range(bridge_length - 1, 0, -1):
                dp[i] = dp[i-1]
            dp[0] = 0
            
            if sum(dp) == 0:
                return time + 1
            else:
                time = time + 1
                continue
        
        for i in range(bridge_length - 1, 0, -1):
            dp[i] = dp[i-1]
        dp[0] = 0
        
        if sum(dp) + truck_weights[num] > weight:    # 다리가 무게를 못 버틸 때
            dp[0] = 0
            time = time + 1
        else:
            dp[0] = truck_weights[num]
            num = num + 1
            time = time + 1
            
    return time


solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10])