class Bank:
    total_balance=100000
    total_loan=0
    loan_status= True

    def __init__(self, name,password) -> None:
        self.name= name
        self.password= password

    def create_acount(self,name, email, address, acType):
        Account(name, email, address, acType)

    def deleteAC(self, acno):
        for user in Account.acounts:
            if user.acNo== acno:
                Account.acounts.remove(user)
                return
        print(f'\nAccount no: {acno} not found\n')
    
    def view_user(self):
        if len(Account.acounts) > 0:
            for user in Account.acounts:
                print(f'AC no: {user.acNo}\nName: {user.name}\n')
    
    def view_bankBalance(self):
        print(f'Total Bank Balance is: {self.total_balance}/=')

    def view_totalLoan(self):
        print(f'Total loan taken is: {self.total_loan}/=')

    def set_loanStatus(self, status):
        Bank.loan_status= status

class Account:
    acounts=[]
    def __init__(self, name, email, address, acType) -> None:
        self.name= name
        self.email= email
        self.address= address
        self.acType= acType
        self.acNo= name+email
        self.balance= 0
        self.transaction_history=[]
        self.loan_count=0
        Account.acounts.append(self)

    def deposit(self, amount):
        if amount > 0:
            self.balance+=amount
            Bank.total_balance+=amount
            print(f'\ntk: {amount}/= Depsited successfully. New Balance is: {self.balance}\n')
            self.transaction_history.append(f'Depsited tk: {amount}/=')
        else:
            print('\nInvalid ammount\n')

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance-=amount
            print(f'\nTK: {amount}/= withdrawn successfully. New Balance is: {self.balance}\n')
            self.transaction_history.append(f'Withrawed tk: {amount}/=')
        else:
            print('\nInsufficient Balance\n')

    def check_balance(self):
        print(f'\nBalance is tk: {self.balance}\n')

    def view_transaction_history(self):
        if len(self.transaction_history) > 0:
            for history in self.transaction_history:
                print(history)
        else:
            print('\nNo Transaction History\n')

    def take_loan(self, amount):
        if Bank.total_balance > amount:
            self.balance+=amount
            Bank.total_balance-=amount
            Bank.total_loan+=amount
            print(f'\nTK: {amount}/= has taken as loan successfully. New Balance is: {self.balance}\n')
            self.transaction_history.append(f'Loan tk: {amount}/=')
        else:
            print('\nThe bank is Bankrupt\n')

    def transfer(self,acn,amount):
        if self.balance > amount:
            for user in Account.acounts:
                if user.acNo== acn:
                    user.balance+=amount
                    self.balance-=amount
                    self.transaction_history.append(f'transfered {amount}/= transfered to {acn}')
                    print(f'\nTk {amount} transfered to {acn}. New Balance is: {self.balance}\n')
                    return
            print(f'AC {acn} not found')
        else:
            print('\nInsufficient Balance to transfer.\n')

admin= Bank('Admin', 1234)
currentUser= None
while True:
    if currentUser== None:
        print('\nNo User Logged in')
        ch=input('\nRegistar/Log-in (R/L/A)')
        if ch=="R":
            name=input('Enter name: ')
            email= input('Enter email: ')
            address= input('Enter address: ')
            acType= input('Enter AC type: ')
            currentUser= Account(name, email, address, acType)
        elif ch=="L":
            acn= input('Enter account no.: ')
            flag= True
            for user in Account.acounts:
                if user.acNo== acn:
                    currentUser=user
                    flag=False
                    break
            if flag:
                print('\nAccount: {acn} not found')
        elif ch=="A":
            p=int(input('Enter Admin Password: '))
            if p==admin.password:
                currentUser= admin
            else:
                print('\nIncorrect Password')
        else:
            print('\nInvalid Input\n')
    elif currentUser==admin:
        print('\nEnter 0 to Log out\nEnter 1 to Create Account\nEnter 2 to delete acount\nEnter 3 to See All User')
        print('Enter 4 to check bank balance\nEnter 5 to check total loan ammount\nEnter 6 to Change loan status\n')
        u=int(input())
        if u==0:
            currentUser=None
        elif u==1:
            name= input('Enter Name: ')
            email= input('Enter email: ')
            address= input('Enter Address: ')
            acType= input('Enter Account Type: ')
            currentUser.create_acount(name, email, address, acType)
        elif u==2:
            acn=input('Enter account no: ')
            currentUser.deleteAC(acn)
            print(f'\nAC {acn} deleted successfully\n')
        elif u==3:
            currentUser.view_user()
        elif u==4:
            currentUser.view_bankBalance()
        elif u==5:
            currentUser.view_totalLoan()
        elif u==6:
            bl=input('Enter "N" to turn off "Y" to turn on: ')
            if bl=="N":
                currentUser.set_loanStatus(False)
                print('\nLoan feature turned OFF\n')
            elif bl=="Y":
                currentUser.set_loanStatus(True)
                print('\nLoan feature turned ON\n')
            else:
                print('Invalid Input\n')
        else:
            print('Invalid input\n')
    else:
        print('\nEnter 0 to Log out\nEnter 1 to deposit\nEnter 2 to withdraw\nEnter 3 to check balance')
        print('Enter 4 to check transaction history\nEnter 5 to take loan\nEnter 6 to transfer money\n')
        u=int(input())
        if u==0:
            currentUser= None
        elif u==1:
            amnt=int(input('Enter deposit amount: '))
            currentUser.deposit(amnt)
        elif u==2:
            amnt=int(input('Enter withdraw amount: '))
            currentUser.withdraw(amnt)
        elif u==3:
            currentUser.check_balance()
        elif u==4:
            currentUser.view_transaction_history()
        elif u==5:
            if Bank.loan_status:
                amnt=int(input('Enter loan amount: '))
                currentUser.take_loan(amnt)
            else:
                print('\nLoan feature is off\n')
        elif u==6:
            amnt=int(input('Enter transfer amount: '))
            acn=input('Enter acount no: ')
            currentUser.transfer(acn,amnt)
        else:
            print('Invalid input')