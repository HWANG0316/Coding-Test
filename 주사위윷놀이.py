def solve(dice_num, dir):
        
my_map = [
    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28 ,30, 32, 34, 36, 38, 40],  # direct
    [13, 16, 19, 25, 30, 35, 40],          # in a[0][4]   
    [22, 24, 25, 30, 35, 40],              # in a[0][9]
    [28, 27, 26, 25, 30, 35, 40]           # in a[0][14] 
]


dice = list(map(int, input().split()))
print(dice_num)


solve(0,0)