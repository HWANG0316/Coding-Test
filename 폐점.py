def solve():
    
    pass
        
def comb(item):

    item_comb =[]
    max_cost = 0
    
    for i in range(N + 1):
        A_list = []
        B_list = []
        sum_cost = 0
        A_count = item[0][0]
        B_count = item[1][0]
        for j in range(N - i): 
            A_list.append(item[0][2] * 2)
            B_list.append(item[1][2])

        for k in range(N-i, N):
            A_list.append(item[0][2])
            B_list.append(item[1][2] * 2)

        
        for l in range(len(A_list)):
            if A_count - A_list[l] > 0:
                sum_cost = sum_cost + A_list[l] * item[0][1]
                A_count = A_count - A_list[l]
            else:
                pass

            if B_count - B_list[l] > 0:
                sum_cost = sum_cost + B_list[l] * item[1][1]
                B_count = B_count - B_list[l]
            else:
                
                pass

        if sum_cost > max_cost:
            max_cost = sum_cost
        

N = int(input())

item = []
item_comb = []

for i in range(2):
    item.append(list(map(int, input().split())))

item_comb = comb(item)
solve()
