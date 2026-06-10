# --------------
# student class
# --------------

class Student:
    def __init__(self,name, age, scores = None):
        self.name = name
        self.age = age
        self.scores = scores if scores is not None else []
    def add_score(self,score):
        self.scores.append(score)
    def get_average(self):
        if len(self.scores) == 0:
            return 0 
        return sum(self.scores) / len(self.scores)
    def get_grade(self):
        avg = self.get_average()
        if avg >= 90:
            return "Grade A"
        elif avg >= 80:
            return "Grade B"
        elif avg >= 70:
            return "Grade C"
        elif avg >= 60:
            return "Grade D"
        else:
            return "Fail"
    def __str__(self):
        return f"Name: {self.name}| Average: {self.get_average():.1f} |Grade: {self.get_grade()}" 

# ----------
# Car class
# ----------
class Car:
    def __init__(self,make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        print(self.make, self.model, "engine started 🚗")
    def describe(self):
        print("Full car description", self.year, self.make, self.model)
    def age(self):
        return "The car is", 2026 - self.year
    def __str__(self):
        return f"{self.year}, {self.make}, {self.model}"
    
# ---------------
# Student Objects
# --------------- 
student1 = Student("APP", 21)
student1.add_score(90)
student1.add_score(90)
student1.add_score(80)

student2 = Student("ZPW", 21)
student2.add_score(90)
student2.add_score(80)
student2.add_score(88)

student3 = Student("lulu", 21)
student3.add_score(88)
student3.add_score(87)
student3.add_score(78)
print("\n=====Student======")
print()
print(f"{student1.name},average score is, {student1.get_average():.1f}")
print(student1.name,"grade is", student1.get_grade())

# Student 2,3 can add

# ---------------
# Car Objects
# --------------- 
car1 = Car("Japan", "Honda fit", 2008)
car2 = Car("Japan", "Honda Civic", 2018)
car3 = Car("Germany", "BMW", 2020)

print("\n=========car===========")
print(car1)
print(car2)
print(car3)


print()
car1.start()
car2.start()
car3.start()

print()
car1.describe()
print("age", car1.age(),"years")

car2.describe()
print("age", car2.age(),"years")

car2.describe()
print("age", car2.age(),"years")