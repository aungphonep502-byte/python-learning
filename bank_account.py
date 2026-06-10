class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.history = []


    # Functions
    # deposit function
    def deposit(self):
        amount = float(input("Type amount deposit"))
        self.balance += amount
        self.history.append(f"Deposited ${amount}")
        print(f"Sucessfully Deposited {amount}")
        

    # withdraw function
    def withdraw(self):
        amount = float(input("Type amount to withdraw"))
        if amount <= self.balance:
            self.balance -= amount
            self.history.append(f"WIthdraw ${amount}")
            print(f"Sucessfully Withdraw {amount}")
            
        else:
            print("Insufficient balance")

    # view_balance function
    def view_balance(self):
        print(f"Your balance is {self.balance}")

    # history function
    def view_history(self):
        if len(self.history) == 0:
            print("No transcations found")
        else:
            print("\nTranscation History")
            for item in self.history:
                print(item)


# main program
history = []
account = BankAccount("app", 1000)

while True:
    print("\n==========Bank Menu==========")
    print("1. - Deposit")
    print("2. - Withdraw")
    print("3. - View Balance")
    print("4. - History")
    print("5. - Exist")

    choose = input("Choose your option")
    if choose == "1":
        account.deposit()
    
    elif choose == "2":
        account.withdraw()
    
    elif choose == "3":
        account.view_balance()
    
    elif choose == "4":
        account.view_history()

    elif choose == "5":
        print("Exist")
        break
    else:
        print("Invalid Input")
    