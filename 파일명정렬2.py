def solution(files):
    file = []
    
    for i in range(len(files)):
        head, number, tail = "", "", ""    
        num_check = False
        for j in files[i]:
            if j.isdigit() == True:
                number = number + j
                num_check = True
            elif num_check == True:
                tail = tail + j
            else:
                head = head + j
            
        file.append([head, number, tail])  # head number tail append
    file.sort(key = lambda x:(x[0].lower(), int(x[1])))

    result = []
    for i in range(len(files)):
        result.append(file[i][0] + file[i][1] + file[i][2])
    return result

solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"])