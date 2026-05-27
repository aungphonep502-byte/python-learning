type = int(input("Type a number"))
need_marks = 50 - type

if type >= 90 and type <=100:
    print("Distinction")
elif type <=89 and type>=79:
    print("Good") 
elif type <=60 and type == 50:
    print("Normal")
elif type <=49 and type ==1:
    print(f"Fail, You need {need_marks} to pass")
else:
    print("This is invalid value")

i = 3
while i != 0:
    print("meow")
    i = i -1

a = -2 
while a <= 0:
    print ("hello")
    a = a + 1


a = 0
while a < 3:
    print ("Hello")
    a = a + 1

b = 0 
while b < 3:
    print ("less")
    b += 1

for a in [1,2,3]:
    print ("hello")

for a in range (4):
    print ("four")

for _ in range (8):
    print ("hey")

# well structure
print ("meow\n" * 3, end = "") 

while True:
    n = int (input("type a number!"))
    if n < 1:
        continue
    else:
        break

while True:
    a = int (input("Type a number!"))
    if a > 3: 
        break
    for _ in range(a):
        print("Meow")

def main():
    a = old()
    new(a)

def old():
        while True:
            n = int(input("Type a number!"))
            if n > 0:
                break
        return n
def new(n):
        for _ in range(n):
            print("hello")

main()

def main():
    a = old ()
    new(a)

def old():
    while True:
        n = int(input("Type a number!"))
        if n > 0:
            break 
    return n

def new(n):
    for _ in range(n):
        print("hello")
main()


def main():
    a = old()
    new(a)

def old():
    while True:
        n = int(input("Type a numebr!"))
        if n > 0:
            break
    return n
def new(n):
    for _ in range(n):
        print ("good")
main()

for _ in range(5):
    print("hello")

while True:
    a = int(input("type a number!"))
    if a < 3:
        break 

for _ in range(a):
    print("hello")

def main():
    a = old()
    new(a)
def old():
    while True:
        n = int(input("type a number!"))
        if n < 3:
            break
        return n 
def new(n):
    for _ in range (n):
        print("hello")

main()

a = ['aung', 'phone', 'paing']
print (a[0])

a = ["how", "are", "you"]
for _ in a:
    print (_)

student = ["thant pyae shine", "zpw", "acm"]
for _ in range(len(student)):
    print(_ + 1, student[_])


students = ["app","acmd","ec"]
for _ in range(len(students)):
    print(_ + 1, students[_])

students = {"app" : "computing" , 
            "zpw" : "computing" , 
            "ec" : "computing" , 
            "nyein" : "bit" ,
            "thiha" : "bit"
            }

users = input("type your name!")
if users == "app":
    print ("computing")
elif users == "thiha":
    print ("bit")
else:
    print ("who?")

students = {"app" : "computing" , 
            "zpw" : "computing" , 
            "ec" : "computing" , 
            "nyein" : "bit" ,
            "thiha" : "bit"
            }

# print (students ["app"])
# print (students["thiha"])
for student in students:
    print(student, students[student], sep = ",")


students = {"app" : "dc",
     "zpw" : "dc",
     "thiha" : "bit",
     "nyein" : "bit"}

for student in students:
    print (student, students[student], sep = ",")

students =[
{"name" : "app", "major" : "IT", "address" : "NorthOkkalapa"},
{"name" : "zpw", "major" : "IT", "address" : "Myaynekon"}, 
{"name" : "thiha", "major": "BIT", "address" : "Junction City"} ]

for student in students:
    print (student["name"], student["major"], student ["address"], sep = ",")

def main():
    a = old()
    
def old():
    while True:
        n = int(input("type a number!"))
        if 1<= n <= 10:
                print(f"the numebr of {n} *2 is, {n *2}")
                break
main ()
            
students = [{"name" : "app", "major" : "IT", "address" : "NorthOkkalap0"},
            {"name" : "zpw", "major" : "IT", "address" : "Timecity"},
            {"name" : "thiha", "major" : "BIT", "address" : "Junction_city"}]

for student in students:
    print(student["name"], student["major"], student["address"], sep = ",")

def main ():
    height(3)

def height(hello):
    print("hi\n" * hello, end ="")
main ()


def main():
    old(5)
def old(hey):
    print("hi\n" * hey, end ="")
main()

def main ():
    print_square(3)
def print_square(n):
    # row in square
    for n in range(3): 
        # brick in row
        for j in range(3):
            print("#", end ="")
        print()
main()

def main ():
    print_square(3)

def print_square(b):
    for b in range(3):
        for b in range(3):
            print("a", end="")
        print()
main()

def main ():
    print_square(3)
def print_square(a):
    for a in range(3):
        for a in range(3):
            print("square", end = "")
        print()
main()

def main():
    print_square(3)
def print_square(size):
    for a in range (size):
        print_width(size)
def print_width(c):
        print("hi" * c)
main()

def main ():
    print_square(3)
def print_square(a):
    for b in range(a):
        print_row(a)
def print_row(c):
    print("hello" * c )

main()

def main():
    print_square(4)
def print_square(a):
    for b in range(a):
        print_row(a)

def print_row(c):
    print("hi" * c)
main()

def main():
    for a in range(10):
        print(a + 1)
main()

def main():
    for a in range (10):
        if a%2== 0:
            print(a)
main()

for a in range (10,0,-1):
    print(a)

a = "Yangon"
for b in range(len(a)):
    print(b+1)

for a in ("Yangon"):
    print(a)

for a in range(10):
    print(a)

a = 1

while a <= 10:
    print (a)
    a += 1

a = 1
while a <= 10:
    print(a)
    a += 1

for a in range(10,0,-1):
    print (a)

a = 1 
while a <= 10:
    print(a)
    a += 1

while True:
    a = input("type quiet")
    if a == "quiet":
        break
    print("You typed", a)

while True:
    a = int(input("Type number "))
    if a == 3:
        continue
    else:
        break

for a in range (1,5):
    if a ==3:
        continue
    print(a)

while True:
    print("hello")

    fruits = ["apple", "banana", "strawbarry"]
    for a in fruits:
        print(a) 

    for a in "banana":
        print(a)

    a =["apple", "banana", "strawberry"]
    for n in a:
        if n == "banana":
            # break
            continue
        print(n)

    for a in range(5):
        print (a)

    for b in range (1,6):
        print (b)

    for c in range (1,20,3):
        print (c)

    for a in range (5):
        print (a)
    else:
        print("finished")

    for a in range (10):
        if a ==3: break
        print(a)
    else:
        print("finish")

    a = ["good", "nice", 'excellent']
    b = ["car","bike", "TV"]

    for x in a:
        for y in b:
            print (x,y)

    for a in [1,2,3]:
        pass

    a = 1
    while a < 5:
        a += 1
        if a ==3:
            continue
        print(a)

    a = 1
    while a < 5:
        print(a)
        if a ==3:
            break
        a += 1

    a= 1
    while a < 5:
        print (a)
        if a ==3:
            break
        a += 1

    i = 1
    while i < 6:
        print(i)
    if i == 3:
        break
    i += 1

    i = 0
    while i < 6:
        i += 1
    if i == 3:
        continue
    print(i)

    a= 0
    while a < 6:
        a += 1
        if a == 3:
            continue
        print(a)

    a = 0 
    while a < 6:
        a += 1 
        if a ==3:
            continue
        print(a)

    a = 0
    while a < 6:
        print(a)
        if a ==3:
            break
        a += 1

    a = 0 
    while a < 6:
        a += 1
        if a ==3:
            continue
        print(a)

    a = 0
    while a < 6:
        print(a)
        a += 1
    else:
        print("a is less than 6 ")

    a = "hello"
    for b in a:
        print(b)

    a = "hello"
    for b in a:
        print(b)
        print("---")

    a = "hello"
    print(a)
    a += "!"
    print(a)

    a= "hello"
    b = ""

    for c in a:
        b =  b+ c
        print (b)   

    for a in range (1,21,2):
        print(a)

    b = 0
    for a in range (1,101):
        b = b + a
    print(b)

    total = 0

    for i in range(1, 101):
        total = total + i

    print(total)

    b = 3
    for a in range (1,11):
        result = a * b 
        print (result)