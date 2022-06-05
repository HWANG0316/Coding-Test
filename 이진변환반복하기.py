def solution(s):
    count = 0
    zero_count = 0 
    while int(s) != 1:
        temp = len(s)
        s = s.replace("0","")
        zero_count = zero_count + temp - len(s)
        s = format(len(s),'b')
        count = count + 1
        
    return [count,zero_count]