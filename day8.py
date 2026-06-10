class School:
    def __init__(self):
        self.name = "KMD"
        self.students_numbers= 1000
    
School1 = School()
print(School1.name)

# Instance Methods
# Methods are functions inside a class.
class Shoool:
    def __init__(self,name):
        self.name = name

    def greet(self):
        print("Hello,", self.name) 
    
Shoool1 = Shoool("Aung")
Shoool1.greet()

# another example
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    def greet(self):
        print(self.grade,self.name)
    
stu1 = Student("Grade A", "Aung")
stu2 = Student("Grade B", "Drew")

stu1.greet()
stu2.greet()
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def show_balance(self):
        print("Balance:", self.balance)
account1 = BankAccount("app", 10000)
account1.show_balance()
account1.deposit()

# Each Object Has Independent Data
class students:
    def __init__(self,name):
        self.name = name
    
student1 = students("Aung")
student1.name = "Phone"
print(student1.name)

class student:
    def __init__(self,name):
        self.name = name

stu1 = student("Aung")
stu1.name = "APP"
print(stu1.name)

# Using __str__
class student:
    def __init__(self, name):
        self.name = name 
    def __str__(self):
        return f"Student: {self.name}"

student1 = student("aung")
print(student1)

class student:
    def __init__(self, name):
        self.name = name 
    def __str__(self):
        return f"Student: {self.name}"
    
stu1 = student("aung")
stu1.name = "paing"
print(stu1)

# Class variables are shared by all objects.
class schools:
    school = "ABCD"

    def __init__(self,name):
        self.name = name
stu1 = schools("aung")
stu2 = schools("paing")

print(stu1.school)
print(stu2.school)

# Instance Variable vs Class Variable
class phones:
    brand = "Apple"

    def __init__(self, model):
        self.model = model 

phone1 = phones("S26 ultra")
phone2 = phones("Iphone 17 pro max")

phone1.model = "Oppo"
print(phone1.brand)
print(phone1.model)
# __str__ and __repr__ Together
class phones:
    def __init__(self,model):
        self.model = model
    def __str__(self):
        return f"Phone model :{self.model}"
    def __repr__(self):
        return f"Phone model is ('{self.model}')"
    
phone1 = phones("apple")
# phone2 = phones("samsung")
print(phone1)
print([phone1])

class students:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f" student name:{self.name}"
    def __repr__(self):
        return f"student name is({self.name})"

stu1 = students("aung")
stu1 = students("aung phone paing")
stu2 = students("drew") 

print(stu1)
print([stu1])

# mini project
class school:
    school = "NCC"
    student_count = 0
    def __init__(self,name, age):
        self.name = name 
        self.age = age 
        school.student_count += 1

    def __str__(self):
        return f"{self.name} : ({self.age})"
    
stu1 = school("APP", 23)
stu2 = school("Drew", 24)
print(stu1,stu2)
print(school.student_count)
# day7 project 
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.history = []
    
    def __str__(self):
        return f"{self.name} : ({self.balance})"

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

user1 = BankAccount("App", 10000)
user2 = BankAccount("Drew", 8000)



user1.deposit()
user1.withdraw()


user2.deposit()
user2.withdraw()

print("======\n Account Summary=======")
print(user1) 
print(user2)

# show balance
print("======\n show balance=======")
user1.view_balance()
user2.view_balance()

print("=======\n Show History =========")
user1.view_history()
user2.view_history()
