from datetime import datetime

ledgers = ["01/01 4 50000", "01/11 6 3555", "02/01 0 -23555", "02/25 5 5000", "03/25 0 -15000", "06/09 8 43951", "12/30 9 99999"]

def solution(ledgers):
    answer = 0
    info = [[0 for i in range(3)] for j in range(len(ledgers))]
    bank = []
    rate = []
    dat = []

    for i in range(len(ledgers)):
        temp = ledgers[i].split(' ')
        temp2 = temp[0].split('/')
        temp2 = "2021" + temp2[0] + temp2[1]

        info[i][0] = temp2
        info[i][1] = int(temp[1]) / 100
        info[i][2] = int(temp[2])


    for i in range(len(ledgers)):
        if info[i][2] >0:
            dat.append(info[i][0])
            rate.append(info[i][1])
            bank.append(info[i][2])
        else:
            money = info[i][2]
            
            for_len  = len(bank)
            for l in range(for_len - 1, -1, -1):
                now = datetime.strptime(info[i][0], "%Y%m%d")
                before = datetime.strptime(dat[l], "%Y%m%d")
                date_diff = now - before
                if bank[l] + money >= 0:
                    bank[l] = bank[l] + money
                    answer = int(answer + (-money* rate[l]) * (date_diff.days / 365))
                else:
                    money = money + bank[l]
                    answer = int(answer + (bank[l] * rate[l]) * (date_diff.days / 365)) 
                    rate.pop()
                    bank.pop()
                    dat.pop()
    
    for i in range(len(dat)-1, -1, -1):
        now = datetime.strptime("20211231", "%Y%m%d")
        before = datetime.strptime(dat[i], "%Y%m%d")
        date_diff = now - before
        answer = int(answer + (bank[i]* rate[i]) * (date_diff.days / 365))
        
    return answer

result = solution(ledgers)
print(result)