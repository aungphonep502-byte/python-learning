'''class Person:
    def __init__(self,name,age):
        self.name = name
        self.__age = age

    def introduce(self):
        return f"Hello, {self.name}"
    @property
    def age(self):
        return self.__age

class Student(Person):
    def __init__(self,name,age,grade):
        super().__init__(name,age)
        self.grade = grade 
    
    def introduce(self):
        return f"Hello, My name is{self.name} and My grade is {self.grade}"

student = Student("APP",20,90)
print(student.age)
print(student.introduce())


try:
    age = int(input("Enter age"))
except:
    print("Invalid input")
    
try:
    age = int(input("Type a number"))
except ValueError as e:
    print("Error:",e)

try:
    age = int(input("type age:"))
except ValueError:
    print("error")

try:
    age =int(input("type a number"))
except ValueError:
    print("invalid input")
else:
    print("your age is",age)

try:
    age =int(input("type a number"))
except ValueError as e:
    print("Error",e)


# else
# Runs only when NO error occurs

try:
    age = int(input("type age:"))
except ValueError:
    print("Invalid Input")
else:
    print("Your age is",age)


# finally
# Runs no matter what.

try:
    age = int(input("Type age:"))
except ValueError:
    print("Invalid Value")
finally:
    print("Program finished")

# Full Example
try:
    age = int(input("Type age"))
except ValueError as e:
    print("Error", e)
else:
    print("You Typed your age is",age)
finally:
    print("Thank you for using the program")

# Practice 1
try:
    number = int(input("type a number"))
    print(number * 2)
except ValueError:
    print("Type valid integer only")

# Practice 2
try:
    number1 = int(input("Type a number"))
    number2 = int(input("Type a number"))
    result = number1 / number2
except ValueError:
    print("Type integer only")
except ZeroDivisionError:
    print("Zero cannot divided")
else:
    print("Result:",result)
finally:
    print("Calculation finished")

raise ValueError("Age cannot be negative")

# Using raise Inside a Function
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    print("Valid Age")

try:
    check_age(-1)

except ValueError as e:
    print("error",e)

class InvalidGradeError(Exception):
    pass

def show_grade(grade):
    if grade <0 or grade >100:
        raise InvalidGradeError("Grade must be between 0 and 100")
    print("Valid Grade")


class InvalidGradeError(Exception):
    pass


def check_grade(grade):
    if grade < 0 or grade > 100:
        raise InvalidGradeError("Grade must be between 0 and 100")

    print("Valid grade")
try:
    check_grade(120)
except InvalidGradeError as e:
    print("Grade Error",e)


class InvalidGradeError(Exception):
    pass
def check_grade(grade):
    if grade <0 or grade >100:
        raise InvalidGradeError ("Grade must be between 0 and 100")
    print("Valid Value")
try:
    check_grade(-1)
except InvalidGradeError as e:
    print("Error",e)

    # Complete Example Bank Transcation
class InvalidBalanceError(Exception):
    pass 
def withdraw(amount,balance):
    if balance < amount:
        raise InvalidBalanceError("Withdraw amount exceed balance")
    return amount - balance
try:
    new_balance = withdraw(1000,5000)
except InvalidBalanceError as e:
    print("Invalid Valid error",e)
else:
    print("New Balance",new_balance)
finally:
    print("Transcation completed")

# practice age error
class InvalidAgeError(Exception):
    pass
def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be at least 18 years old!")
    print ("Valid Value")
try:
    check_age(27)
except InvalidAgeError as e:
    print("Invalid Age Error",e)
else:
    print("Registration successful")
finally:
    print("Registraction Completed")

# practice with negative number error
class NegativeNumberError(Exception):
    pass
def SquareRoot(number):
    if number < 0:
        raise NegativeNumberError("Number must be positive to be square root")
    return number ** 0.5
try:
    new_number = SquareRoot(4)
except NegativeNumberError as e:
    print("Error",e)
else:
    print("successfully square root",new_number)
finally:
    print("Program finished")

    
# Validate a Number Input
while True:
    try:
        text = input("Type a number")
        
        if text == "":
            print("Text must not be empty")
            continue
        num = float(text)
        break 
    except ValueError:
        print("Please enter a valid value")


# Validate an Operator
while True:
    operation = input("Type like + - * /")
    if operation in ["+", "-", "*","/"]:
        break 
    print("Invalid Operator")


# Bulletproof Calculator
while True:
    try:
        first = input("Type first number")
        if first == "":
            print("first number must not be empty")
        num1 = float(first)

        second = input("Type second number")
        if second == "":
            print("second number must not be empty")
        num2 = float(second)
        operation = input("Type (+ - * /)")
        if operation == "+":
            print("Result:", num1 + num2)
        elif operation == "-":
            print("Result:",num1)
        elif operation == "*":
            print("Result:", num1 * num2)
        elif operation == "/":
            print("Result:",num1 / num2)
        else:
            print("Invalid Error")
    except ValueError:
        print("Number Only Please")
    except ZeroDivisionError:
        print("Cannot divided by zero")
    choice = input("Continue? y/n")
    if choice != "y":
        break
        


# Better Version Using a Function
def get_input(prompt):
    while True:
        try:
            text = input(prompt)

            if text == "":
                print("Text must not be empty")
                continue 

            return float(text)
        
        except ValueError:
            print("please enter a valid number")
        
num1 = get_input("First number")
num2 = get_input("second number")

def get_number(prompt):
    while True:
        try:
            text = input(prompt)
            if text == "":
                print("Text not must be empty")
            return float(text)

        except ValueError:
            print("Please enter a valid number")  

num1 = get_number("first number")
num2 = get_number("second number")


def get_number(prompt):
    while True:
        try:
            text = input(prompt)
            if text == "":
                print("Text must not be empty")
                continue 
            return float(text)
        except ValueError:
            print("please enter a valid value")
num1 = get_number("first numeber")
num2 =  get_number("second number")



def get_number(prompt):
    while True:
        try:
            text = input(prompt)
            if text == "":
                print("Text not must be zero")
                continue
            return float(text)
        except ValueError:
            print("Please enter a valid value")
num1 = get_number("First Number")
num2 = get_number("Second Number")

# Test Cases
def get_number(prompt):
    while True:
        try:
            text = input(prompt)
            if text == "":
                print("text not must be empty")
            return float(text)
        except ValueError:
            print("Input must be valid data")
num1 = get_number("First number")
num2 = get_number("second number")

operator = input("operators (+ - * /)")
if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    if num2 ==0:
        print("cannot divided by 0")
    else:
        print(num1/num2)
else:
    print("invalid data")

def combine(prompt):
    while True:
        try:
            text = input(prompt)

            if text == "":
                print("Text must not be empty")
                continue 
            return float(text)

        except ValueError:
            print("Please enter valid data")

num1 = combine("First number")
num2 = combine("Second number")

operator = input("Type (+ - * /)")

if operator == "+":
    print("Result",num1 + num2)
elif operator == "-":
    print("Result",num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    if num2 == 0:
        print("Cannot divided by zero")
    else:
        print(num1 / num2)

else:
    print("Invalid input")

'''
