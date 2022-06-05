def solution(brown, yellow):
    area = brown + yellow
    print(area)
    
    for i in range(3,3 + yellow):
        if area % i == 0:
            w = area / i
            h = i
            
            yellow_w = w -2
            yellow_h = i - 2
            
            if yellow_w * yellow_h == yellow:
                return [w,h]