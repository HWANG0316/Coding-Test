import itertools

N = int(input())

n_list = [] # 숫자 리스트
opt = [] # 연산자 리스트
opt_num = [] # 연산자 개수
n_list = (list(map(int, input().split())))
opt_num = (list(map(int, input().split())))

for i in range(4):
    for j in range(opt_num[i]):
        if i == 0:
            opt.append("+")
        elif i == 1:
            opt.append("-")
        elif i == 2:
            opt.append("*")
        elif i == 3:
            opt.append("/")


nPr = itertools.permutations(opt, len(n_list) - 1)
nPr = list(nPr)

result_list = []
count = 0
result = 0
for i in range(len(nPr)):
    count = 1
    result = n_list[0]
    for j in range(len(nPr[0])):

        if nPr[i][j] == "+":
            result = result + n_list[count]
            count = count + 1
        elif nPr[i][j] == "-":
            result = result - n_list[count]
            count = count + 1
        elif nPr[i][j] == "*":
            result = result * n_list[count]
            count = count + 1
        elif nPr[i][j] == "/":

            if result < 0:
                result = -(abs(result) // n_list[count])
                count = count + 1
            else:
                result = result // n_list[count]
                count = count + 1


    result_list.append(result)

print(max(result_list))
print(min(result_list))
