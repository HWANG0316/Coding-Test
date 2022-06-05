def solution(numbers):
    
    for i in range(len(numbers)):
        numbers[i] = [str(numbers[i]),str(numbers[i]) * 3]
    numbers.sort(key = lambda x: x[1], reverse = True)
    
    result = ""
    for i in numbers:
        result = result + i[0]
    result = int(result)
    result = str(result)
    return result