# Functions
# deposit function
def deposit(account, history):
    amount = float(input("Type amount deposit"))
    account ["balance"] += amount
    print(f"Sucessfully Deposited {amount}")
    history.append(f"Deposited ${amount}")

# withdraw function
def withdraw(account, history):
    amount = float(input("Type amount to withdraw"))
    if amount <= account["balance"]:
        account["balance"] -= amount
        print(f"Sucessfully Withdraw {amount}")
        history.append(f"WIthdraw ${amount}")
    else:
        print("Insufficient balance")

# view_balance function
def view_balance(account):
    print(f"Your balance is {account['balance']}")

# history function
def view_history(history):
    if len(history) == 0:
        print("No transcations found")
    else:
        print("\nTranscation History")
        for item in history:
            print(item)


# main program
history = []
account = {"name":"app",
           "balance":1000}

while True:
    print("\n==========Bank Menu==========")
    print("1. - Deposit")
    print("2. - Withdraw")
    print("3. - View Balance")
    print("4. - History")
    print("5. - Exist")

    choose = input("Choose your option")
    if choose == "1":
        deposit(account,history)
    
    elif choose == "2":
        withdraw(account,history)
    
    elif choose == "3":
        view_balance(account)
    
    elif choose == "4":
        view_history(history)

    elif choose == "5":
        print("Exist")
        break
    else:
        print("Invalid Input")
    