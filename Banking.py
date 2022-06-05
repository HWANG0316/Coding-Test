class User():
    NAME = 'JS'
    PIN_NUM = '1234'
    balance_code = 0
    balance = [0, 0, 0]             # 3가지 계정이 존재한다고 가정(예금, 적금, 청약통장)
    
    def set_balance(self, idx, money):
        self.balance[idx] = money
        
    def get_balance(self, idx):
        return self.balance[idx]
            
    def set_PIN_NUM(self, num):
        self.PIN_NUM = num
    
    def get_PIN_NUM(self):
        return self.PIN_NUM
    
    def set_balance_code(self, code):
        self.balance_code = code
        
    def get_balance_code(self):
        return self.balance_code
        
class Bank(User):
    user = User()
    def __init__(self, User):
        super()
        self.user = User
        print("Welcome to JS Banking System")
        print("Please insert to card")
    
    def check_PIN(self, num, count = 0):
        
        if num == self.get_PIN_NUM():
            return True
        elif num != self.get_PIN_NUM():
            return False
            
        
    def insert_card(self, count = 0):
        
        while count < 5:
            temp_pinnum = input()
            if self.check_PIN(temp_pinnum) == False:
                count = count + 1
                print("Incorrect your PIN NUMBER. Please insert to correct PIN NUMBER")
            elif self.check_PIN(temp_pinnum) == True:
                print("Correct your password. You can spend our Banking System ")
                return
            
        print("Incorrect to your PIN Number 5 times. Sorry restart Banking System")        
        return 
                

    def select_account(self, count = 0):
        num = 0
        
        while count < 3:
            print("select your service code")
            print("1. deposit         2. save           3. subscribe           4. withdraw         5. exit")
            num = int(input())
            if num == 1:
                self.set_balance_code(1)
                return
            elif num == 2:
                self.set_balance_code(2)
                return
            elif num == 3:
                self.set_balance_code(3)
                return
            elif num == 4:
                self.set_balance_code(4)
                return
            elif num == 5:
                self.set_balance_code(5)
                return
            else:
                print("Sorry. this balance code not exist\n")
                count = count + 1
                
        print("Incorrect to your account code 3 times. Sorry restart Banking System")        

    def play(self):
        while self.balance_code != 5:
            self.select_account() 
            
            if self.balance_code == 5:
                return
            
            balance_code_name = ["deposit", "save", "subscribe","withdraw", "exit"]
            print("You choice to {0} service".format(balance_code_name[self.get_balance_code() - 1]))
            
            if self.get_balance_code() == 4:
                print("Please input the code to withdraw money")
                where = int(input())
                
                print("Please input the money to {0}".format(balance_code_name[self.get_balance_code() - 1]))
                money = int(input())
                self.withdraw(where, money)
            else:
                print("Please input the money to {0}".format(balance_code_name[self.get_balance_code() - 1]))
            

                money = int(input())
                if self.get_balance_code() == 1:
                    self.deposit(money)
                elif self.get_balance_code() == 2:
                    self.save(money)
                elif self.get_balance_code() == 3:
                    self.subscribe(money)
                    
    def deposit(self, money):
        self.set_balance(self.get_balance_code() - 1, self.get_balance(self.get_balance_code() - 1) + money)
    
    def save(self, money):
        self.set_balance(self.get_balance_code() - 1, self.get_balance(self.get_balance_code() - 1) + money)
    
    def subscribe(self, money):
        self.set_balance(self.get_balance_code() - 1, self.get_balance(self.get_balance_code() - 1) + money)
    
    def info_my_account(self):
        print("Your account is ", end ="")
        print(self.balance) 
        

    def withdraw(self, where, money):
        if self.get_balance(where-1) - money < 0:
            print("Sorry, balance is not enough to withdarw this money")
        else: 
            self.set_balance(where - 1, self.get_balance(where-1) - money)
            

if __name__ == '__main__':
    JS = User()
    JS_BANK = Bank(JS)                        # Bank 객체 생성 (은행 방문)
    JS_BANK.insert_card()
    JS_BANK.play()
    JS_BANK.info_my_account()


    