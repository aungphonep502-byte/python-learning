# custom exceptions 
class InsufficientFundError(Exception):
    pass
class InvalidAmountError(Exception):
    pass
class AccountNotFoundError(Exception):
    pass

# BankAccount Class
class BankAccount:
    def __init__(self,account_number,owner,balance=0):
        self.account_number = account_number
        self.owner = owner 
        self.__balance = balance
        self.history = []

    @property 
    def balance(self):
        return self.__balance
# Update deposit()
    def deposit(self,amount):
        if amount <= 0:
            raise InvalidAmountError(
                "Deposit amount must not be zero"
            )
        self.__balance += amount 
        self.history.append(f"Deposit amount,{amount}")

# Update withdraw()
    def withdraw(self,amount):
        if amount <= 0:
            raise InvalidAmountError(
                "Withdraw amount must not be zero"
            )
        if self.__balance < amount:
            raise InsufficientFundError(
                "Fund error"
            )
        self.__balance -= amount
        self.history.append(f"Withdraw amount:,{amount}")
# history
    def show_history(self):
        if not self.history:
            print("No Transcation")
        else:
            print("\n========Transcation History=========")
            for items in self.history:
                print(f"- {items}")


# ATM Class
class ATM:
    def __init__(self):
        self.accounts ={}
    def add_account(self,account):
        self.accounts[account.account_number] = account
    def get_account(self,account_number):
        if account_number not in self.accounts:
            raise AccountNotFoundError(
                "Account does not exist"
            )
        return self.accounts[account_number]
    
# ==========================
# Helper Function
# ==========================
def get_amount(prompt):
        while True:
            try:
                text = input(prompt)
                if text == "":
                    print("Not must be empty")
                    continue 
                amount = float(text)
                return amount
            except ValueError:
                print("Please enter a valid data")

# ==========================
# Create ATM and Accounts
# ==========================
atm = ATM()
atm.add_account(
    BankAccount("1001","APP",10000
    )
)
atm.add_account(
    BankAccount("1002","YST",15000
    )
)

# ==========================
# Main Program
# ==========================
while True:
    error_message = ""
    try:
        print("\n========ATM Menu=========")
        print("1: Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. View History")
        print("5. Exist")

        choice = input("Choice your option")
        if choice == "":
            print("Not must be empty")
            continue
        choice = int(choice)

        if choice == 5:
            print("Good Bye, Have a great day!")
            break

        account_number = input("Type an account number!")
        account = atm.get_account(
            account_number
        )  

# -------------------
# Check Balance
# -------------------
        if choice == 1:
            print(
                f"Owner:,{account.owner}"
            )
            print(
                f"Balance,{account.balance}"
            )
# -------------------
# Deposit
# -------------------
        elif choice == 2:
            amount = get_amount(
                "Deposit amount"
            )
            account.deposit(amount)
            print(
                "Deposit successsful"
            )
            print(
                f"New Balance,{account.balance}"
            )

# -------------------
# Withdraw
# -------------------
        elif choice ==3:
            amount = get_amount(
                "Withdraw amount"
            )
            account.withdraw(amount)
            print(
                "Withdraw successful"
            )
            print(
                f"New Balance,account.balance"
            )
# -------------------
# History
# -------------------
        elif choice == 4:
            account.show_history()
        
        else:
            print("Invalid input")
    
    except InsufficientFundError as e:
        error_message = str(e)
        print(
            f"Fund error,{e}"
        )
    except AccountNotFoundError as e:
        error_message = str(e)
        print(
            f"Account does not Exist,{e}"
        )
    except InvalidAmountError as e:
        error_message = str(e)
        print(
            f"Amount error,{e}"
        )
    except ValueError as e:
        error_message = str(e)
        print(
            f"Data must be valid data"
        )
    finally:
        if error_message:
            with open(
                "errors.txt","a"
            ) as file:
                file.write(
                    error_message+"\n"
                )
