def solution(m, musicinfos):
    result = []
    time_lst = []
    for i in musicinfos:
        start, finish, name, code = i.split(',')
        temp_code = ""
        time = int(finish[3:]) - int(start[3:])
        temp_time = time
        time_lst.append(time)

        for j in range(time):
            if code[j %len(code)] == "#":
                temp_code = temp_code + "#"
                temp_time = temp_time + 1
            else:
                temp_code += code[j % len(code)]

        for j in range(time, temp_time):
            if code[j %len(code)] == "#":
    
                temp_code = temp_code + "#"
                temp_time = temp_time + 1
            else:
                temp_code += code[j % len(code) ]
        idx = temp_code.find(m) + len(m) -1
        if m in temp_code and temp_code[idx + 1] != '#':
            result.append([name, time])
    
    result.sort(key = lambda x:x[1])
    return result[0][0]


print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
#print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
#print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))