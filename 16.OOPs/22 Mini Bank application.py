# Mini bank application

class Customer:
    ''' Mini bank application to demonstrate oop concept'''
    bankName = 'DurgaBank'

    def __init__(self, name , balance=0.0):
        self.name = name
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        print(f'{amount}/- has been deposited. Available balance is {self.balance}/-.')

    def withdraw(self,amount):
        if amount > self.balance:
            print(f'Transaction failed.. Insufficient funds in account.')
        else:
            self.balance -= amount
            print(f'{amount}/- has been withdrawn. Available balance is {self.balance}/-.')

    def checkBalance(self):
        print(f'Available balance is {self.balance}/-')


print(f'Welcome to {Customer.bankName}!!')
name = input('Enter your name : ')
c1 = Customer(name)

while True:
    print(f'\nPress 1 to deposit. \nPress 2 to withdraw. \nPress 3 to check balance. \nPress 4 to exit. ')
    option = int(input('Enter option: '))
    if option == 1:
        amount = float(input('Enter amount to be deposited: '))
        c1.deposit(amount)
    elif option == 2:
        amount = float(input('Enter amount to be withdrawn : '))
        c1.withdraw(amount)
    elif option == 3:
        c1.checkBalance()
    elif option == 4:
        print(f'Thanks for using {Customer.bankName}.')
        break
    else:
        print('Invalid selection. Retry your selection.')

