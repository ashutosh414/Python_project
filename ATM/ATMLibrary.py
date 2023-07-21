#simple ATM details:

class Atm:

    # Constructor: It s a special method which will autoicaally executed if we make obbect of its class
    def __init__(self):
        self.pin=""
        self.balance=0

        print(id(self))

        self.menu()
        

    def menu(self):
        user_input=input('''
            How would like to proceed?
            1. Enter to create PIN
            2. Enter to Deposite
            3. Enter to Withdraw
            4. Enter to check Balance
            5. Enter to EXIT
    ''')
        if user_input=='1':
            self.create_pin()
        elif user_input=='2':
            self.deposit()
        elif user_input=='3':
            self.withdraw()
        elif user_input=='4':
            self.check_balance()
        elif user_input=='5':
            print('Thanks')
        else:
            print("enter valid input")
            self.menu()

    def create_pin(self):
        confirm_pin=input("Enter your PIN")
        reconfirm_pin=input("Reconfirm your PIN")
        if confirm_pin==reconfirm_pin:
            self.pin=confirm_pin
            print("PIN SET SUCCESSFUL")
        self.menu()
    
    def deposit(self):
        temp=input("Enter your PIN")
        if temp==self.pin:
            amount=int(input("Enter the deposite amount"))
            self.balance=self.balance+amount
            print("Deposite Successful")
        else:
            print('Invalid PIN')
        self.menu()
    
    def withdraw(self):
        temp=input("Enter your PIN")
        if temp==self.pin:
            amount=int(input("Enter the withdrawl amount"))
            if amount< self.balance:
                self.balance=self.balance-amount
                print("Deposite Successful")
            else:
                print('Insufficient balance')
        else:
            print('Invalid PIN')
        self.menu()

    def check_balance(self):
        temp=input("Enter your PIN")
        if temp==self.pin:
            print(f'Your amount is {self.balance}')
        else:
            print("Invalid PIN")
        self.menu()

