class Student:
    school_name = "KMD"
    def __init__(self,name, scores=None):
        self.name = name
        self.scores = scores if scores is not None else []
    def add_score(self,score):
        self.scores.append(score)
    def avg_score(self):
        if len(self.scores) == 0:
            return 0
        return sum(self.scores) / len(self.scores)
    def __str__(self):
        return f"{self.name} {self.avg_score():.1f}"
# ======
# object
# ======
student1 = Student("app")
student1.add_score(90)
student1.add_score(80)
student1.add_score(88)

student2 = Student("lulu")
student2.add_score(90)
student2.add_score(80)
student2.add_score(78)

print("\n==========Students===========")
print(student1.__str__())
print(student2.__str__())

print("\n==========Students' School===========")

print("School of app is",student1.school_name)
print("School of lulu is",student2.school_name)


print("\n==========Students' Avgerage Scores===========")
print(f"Avgerage score of app is,{student1.avg_score():.1f}")
print(f"Avgerage score of lulu is,{student2.avg_score():.1f}")

# Inheritance + super() 
class Person:
    def __init__(self,name):
        self.name = name
class Student(Person):
    def __init__(self,name,grade):
        super().__init__(name)
        self.grade = grade 

student1 = Student("App",90)

# Add Child Method
class Person:
    def __init__(self, name):
        self.name = name
    def introduce(self):
        print(f"My name is {self.name}")

class Student(Person):
    def __init__(self,name,grade):
        super().__init__(name)
        self.grade = grade
    def show_grade(self):
        print(f"Grade is {self.grade}")

# Child Uses Parent Method
student1 = Student("APP",90)
student1.introduce()
student1.show_grade()

# Practice Task
class Vehicle:
    def __init__(self,brand):
        self.brand = brand
    def show_brand(self):
        print(f"Brand is, {self.brand}")
class Car(Vehicle):
    def __init__(self,brand,model):
        super().__init__(brand)
        self.model = model
    def show_model(self):
        print(f"model is {self.model}")

car1 =Car("Insight",2020)
car2 =Car("BMW", 2023)

car1.show_brand()
car1.show_model()

car2.show_brand()
car2.show_model()

# Method Overriding
class Animal:
    def sound(self):
        print("Animal makes sound")
class Dog(Animal):
    def sound(self):
        print("Dogs bark")
dog = Dog()
dog.sound()

# isinstance()
class Animal:
    pass
class Dog(Animal):
    pass
dog = Dog()

print(isinstance(dog,Dog))
print(isinstance(dog,Animal))

# Encapsulation
class BankAccount:
    def __init__(self):
        self.__balance = 10000

# Protected Attributes (_)
class Person:
    def __init__(self,name):
        self._name = name
person = Person("APP")
print(person._name) 

# Private Attributes (__)
class BankAccount:
    def __init__(self):
        self.__balance = 10000
account = BankAccount()
print(account.__balance)

# Access Private Data Using Methods
class BankAccount:
    def __init__(self):
        self.__balance = 10000
    def show_balance(self):
        return self.__balance
account = BankAccount() 
print(account.show_balance())

# @property
class Bankaccount:
    def __init__(self):
        self.__balance = 10000
    @property
    def balance(self):
        return self.__balance

account = Bankaccount()
print(account.balance)

# Polymorphism
class Dog:
    def speak(self):
        print("Wolf")
class Cat:
    def speak(self):
        print("Meow")
Animals = [Dog(),Cat()]
for animal in Animals:
    animal.speak()

# Mini Practice 
class Person:
    def introduce(self):
        print("I am a person")
class Student(Person):
    def introduce(self):
        print("I am a student")

p = Person()
s = Student()

p.introduce()
s.introduce()

class Animal:
    def __init__(self,name):
        self.name = name
    def sound(self):
        print(f"Animal makes sound!") 

class Dog(Animal):
    pass
dog = Dog("PanPan")
print(dog.name)
dog.sound()


class Animal:
    def __init__(self,name):
        self.name = name
    def sound(self):
        print("Animal makes sound") 
class Cat(Animal):
    def sound (self):
        print(f"{self.name} says Meow")
class Dog(Animal):
    def sound(self):
        print(f"{self.name} says WOlf")
cat = Cat("Buddyy")
dog = Dog("MuMu")

cat.sound()
dog.sound()

animals = [
    Dog("Buddy"),
    Cat("MuMu"),
    Dog("Max"),
    Cat("Luna")
]
for animal in animals:
    animal.sound()


































    




