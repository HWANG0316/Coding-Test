def solution(phone_book):
    phone_book.sort()
    first_num = [[] for i in range(10)]
    for i in phone_book:
        first_num[int(i[0])].append(i)     
        
    for i in range(10):
        if len(first_num[i]) == 0 or len(first_num[i]) == 1:
            continue
        
        for j in range(len(first_num[i])):
            if j + 1 <len(first_num[i]):
                if first_num[i][j] != first_num[i][j + 1][:len(first_num[i][j])]:
                    continue
                else:
                    return False               
    return True