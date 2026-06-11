class BankAccount:

    def __init__(self,owner,balance=0):
        self.owner = owner 
        self.__balance = balance
        self.history = []

    @property
    def balance(self):
        return self.__balance
    
    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
            self.history.append(f"Deposit: ${amount}")

    def withdraw(self,amount):
        if  amount <= self.__balance:
            self.__balance -= amount
            self.history.append(f"Withdraw: ${amount}")
        else:
            print("Insufficient funds")
    
    def show_history(self):
        print(f"\n Transcation History for {self.owner}")
        for item in self.history:
            print(item) 
    
    def __str__(self):
        return f"Owner: {self.owner}, Balance: {self.__balance}"

# -------------------
# class savingaccount
# -------------------

class SavingsAccount(BankAccount):
    def __init__(self,owner,balance,interest_rate):
        super().__init__(owner,balance)
        self.interest_rate = interest_rate
    def apply_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.deposit(interest)
    def __str__(self):
        return  (
            f"Saving Account"
            f"Owner: {self.owner}"
            f"Balance: {self.balance:.2f}"
            f"Interest Rate: {self.interest_rate}"
        )

# ============
# loan Account 
# ============

class LoanAccount(BankAccount):
    def __init__(self,owner,balance,loan_limit):
        super().__init__(owner,balance)
        self.loan_limit = loan_limit
    def withdraw(self,amount):
        if self.balance - amount >= -self.loan_limit:

            current = self.balance 
            new_balance = current - amount

            self._BankAccount__balance = new_balance

            self.history.append(f"Withdraw : {amount}")
        else:
            print("Loan Limited Exceeded")
    
    def check_debt(self):
        if self.balance <0:
            print(f"Debt ${abs(self.balance)}")
        else:
            print(f"No Debt")
    
    def __str__(self):
        return (
            f" Loan Account"
            f"Owner: {self.owner}"
            f"Balance:{self.balance}"
            f"Loan Limit: {self.loan_limit}"
        )
# --------------
# Objects
# --------------

account = BankAccount("APP",1000)
account.deposit(500)
account.withdraw(500)
print(account)
print(account.balance)
account.show_history()

print("\n" + "=" * 40)

saving = SavingsAccount("Drew",10000,50)
saving.apply_interest()
print(saving)
print(saving.balance)
print("\n" + "=" * 40) 

loan = LoanAccount("Andrew",100,1000)
loan.withdraw(1200)
loan.check_debt()
print(loan)
print(loan.balance)