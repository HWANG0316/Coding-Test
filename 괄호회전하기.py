def check(my_stack, word):
    
    if word == ')' and my_stack[-1] == '(':
        my_stack.pop()
    elif word =='}' and my_stack[-1] == '{':
        my_stack.pop()
    elif word == ']' and my_stack[-1] == '[':
        my_stack.pop()
    
    return my_stack

def solution(new_id):
    count = 0
    close = [')',']','}']
    
    temp_id = new_id
    for i in range(len(new_id)):
        my_stack = []
        tepm_id = new_id[i:] + new_id[: i]

        if tepm_id[0] in close:
            continue
        
        for j in tepm_id:
            if len(my_stack) != 0 and j in close:
                my_stack = check(my_stack, j) 
            else:
                my_stack.append(j)            
        if len(my_stack) == 0:
            count = count + 1

    return count