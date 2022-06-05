def solution(program, flag_rules, commands):
    
    # program -> (str)
    # flag_rules -> (arr)
    # commands ->(arr)
    
    # flag의 이름과 flag가 받아야 하는 인자의 종류를 묶어 놓은 것을 flag_rule이라고 함.
    # 주어진 명령어가 모든 flag_rule을 지키는지 검사하는 코드를 작성해야함.
    # 각각의 command가 flag_rule을 지키는지 확인해야함.
    
    # 가독성, 확장성, 주석, 테스트가 용이한 코드로 작성해야함.
    # 이미 있는 librarry 사용 금지.
    
    # 1. program으로 시작해야함.
    # 2. flag argument는 대응하는 flag의 flag_argument_type과 일치해야함.
    # 3. flag는 0 or 1
    # 4. 
    
    answer = []
  
    
    for i in range(len(commands)):
        str = commands[i].split()
        
        for j in range(len(str)):
            if isNum(str[j]) == True:
                str[j] = int(str[j])
        
        print(str)
        if str[0] != program:
            answer.append(False)
            break
        
        for j in range(1, len(str)):
            
            if str[j] == "-n" and (str.index(str[j]) + 1 != len(str)):  # -n이고 -n이 마지막 요소가 아닐 때
                if isNum(str[j + 1]) == False:
                    answer.append(False)
                    print(1)
                    break
            
            if str[j] == "-s" and (str.index(str[j]) + 1 != len(str)): # -s이고 -s가 마지막 요소가 아닐 때
                if isStr(str[j + 1]) == False:
                    answer.append(False)
                    print(2)
                    break
            
            if str[j] == "-e":
                if (str.index(str[j]) + 1) == len(str):
                    answer.append(True)
                    break
                
                if str[j + 1] != "-n" or str[j + 1] != "-s" or str[j + 1] != "-e":
                    print(3)
                    answer.append(False)
                    break
                    
            if "-e" not in str and "-n" not in str and "-s" not in str:
                answer.append(False)
                break
            
    return answer


def isNum(num):
    try:
        int(num)
        return True
    except ValueError:
        return False
    
def isStr(st):
    try:
        str(st)
        return True
    except ValueError:
        return False