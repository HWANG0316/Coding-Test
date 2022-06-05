eng_num = ["zero","one","two","three","four","five","six","seven","eight","nine"]
num = ["0","1","2","3","4","5","6","7","8","9"]
idx = ['n'] * 50

def solution(s):
    
    count = 0
    for i in range(50):
         
        if eng_num[count] in s:
            idx[s.find(eng_num[count])] = eng_num[count]
            s = s.replace(eng_num[count],'a' * len(eng_num[count]),1)
            
        if num[count] in s:
            idx[s.find(num[count])] = num[count]
            s = s.replace(num[count], 'a' ,1)
           
        if eng_num[count] not in s and num[count] not in s:
            count = count + 1
            
        if count == 10:
            break
            
    for i in range(50):
        if 'n' in idx:
            idx.remove('n')
    
    for i in range(len(idx)):
        for j in range(10):
            if idx[i] == eng_num[j]:
                idx[i] = num[j]
                break
            
    return int(''.join(idx))