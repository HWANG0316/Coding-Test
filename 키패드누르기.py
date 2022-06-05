from math import sqrt

left_pos = [[0,0],[1,0],[2,0]]
right_pos = [[0,2],[1,2],[2,2]]

left = [1,4,7]
right = [3,6,9]
mid = [2,5,8,0]

def solution(numbers, hand):
    try:
        current_left = [3,0]
        current_right =[3,2]
        result = []
        for i in numbers:
            if i == 1:
                current_left = left_pos[0]
                result.append("L")
            elif i == 4:
                current_left = left_pos[1]
                result.append("L")
            elif i == 7:
                current_left = left_pos[2]
                result.append("L")
            elif i == 3:
                current_right = right_pos[0]
                result.append("R")
            elif i == 6:
                current_right = right_pos[1]
                result.append("R")
            elif i == 9:
                current_right = right_pos[2]
                result.append("R")      ##### 이까지는 문제 없을 듯
            elif i == 2:
                
                if abs(current_left[0] - 0) + abs(current_left[1] -1) == abs(current_right[0] - 0) + abs(current_right[1] - 1):
                    if hand == "right":
                        current_right = [0,1]
                        result.append("R")
                    else:
                        current_left = [0,1]
                        result.append("L")

                elif abs(current_left[0] - 0) + abs(current_left[1] -1) > abs(current_right[0] - 0) + abs(current_right[1] - 1):
                    current_right = [0,1]
                    result.append("R")
                else:
                    current_left = [0,1]
                    result.append("L")
            elif i == 5:
                if abs(current_left[0] - 1) + abs(current_left[1] -1) == abs(current_right[0] - 1) + abs(current_right[1] - 1):
                    if hand == "right":
                        current_right = [1,1]
                        result.append("R")
                    else:
                        current_left = [1,1]
                        result.append("L")


                elif  abs(current_left[0] - 1) + abs(current_left[1] -1) > abs(current_right[0] - 1) + abs(current_right[1] - 1):
                    current_right = [1,1]
                    result.append("R")
                else:
                    current_left = [1,1]
                    result.append("L")
            elif i == 8:
                if  abs(current_left[0] - 2) + abs(current_left[1] -1) == abs(current_right[0] - 2) + abs(current_right[1] - 1):
                    if hand == "right":
                        current_right = [2,1]
                        result.append("R")
                    else:
                        current_left = [2,1]
                        result.append("L")

                elif abs(current_left[0] - 2) + abs(current_left[1] -1) > abs(current_right[0] - 2) + abs(current_right[1] - 1):
                    current_right = [2,1]
                    result.append("R")
                else:
                    current_left = [2,1]
                    result.append("L")
            elif i == 0:
                if abs(current_left[0] - 3) + abs(current_left[1] -1) == abs(current_right[0] - 3) + abs(current_right[1] - 1):
                    if hand == "right":
                        current_right = [3,1]
                        result.append("R")
                    else:
                        current_left = [3,1]
                        result.append("L")

                elif abs(current_left[0] - 3) + abs(current_left[1] -1) > abs(current_right[0] - 3) + abs(current_right[1] - 1):
                    current_right = [3,1]
                    result.append("R")
                else:
                    current_left = [3,1]
                    result.append("L")
            
        return ''.join(result)
    except Exception as e:
        print(e)