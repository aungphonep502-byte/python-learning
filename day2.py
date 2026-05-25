x = input("Username!")
y = input("Age")
z = input("City")
print(f"{x}")
print(f"{y}")
print(f"{z}")

a = "2000"
num = int(a)
print(num)

a = input("Type a number!")
b = input("Type a number!")
total = int (a) * int(b)
print ("The total amount is", total)


# from W3School
1

sum1 = 100 + 200 
sum2 = sum1 + 200
sum3 = sum1 + sum2
print(sum1,sum2,sum3)

# lesson 2

x = 2
y = 2
print (x ** y)
print(x + y)
print(x * y )
print (x // y)
print(x / y)
print (x - y)
print(x % y)

# lesson 3 

x=5
x+= 3 
print(x)

x-= 3
print(x)

x *=3
print (x)

x %=3
print(x)

x /= 3
print(x)

x //= 3 
print(x)

x **= 3 
print (x)

x=20
# x >>= 4
# print(x)

# print (y:=16)
a=10
b=20
c=40
d=50
# Xor
# x ^= 3  
y=10
x ^= 3
a >>= 3
b <<= 3
c &= 3 
d |= 3
print(x)
print (y)
print(a)
print(b)
print(c)
print(d)

# if statement with len function 
a = [1,2,3,4,5]

if(count:=len(a)) > 3:
    print (f"lis has{count} number")

# comparison operators
x=10
y=5 
print(x == y)
print (x != y) 
print(x > y )
print(x < y) 
print(x >= y) 
print(x <= y )

a = 5
print(1<a<10)
print(1<a and a<10)

# and or not lessons
a=10
print(a>1 and a<11)

print(a>1 or a<10)

print (not(a>11 and a<1))

# From official CS50P 

a = int(input("What's a?"))
b = int(input("What's b?"))

if a > b:
    print("a is greater than b")
elif a < b:
    print("a is less than b")
else:
    print ("a is equal to b")

x = int(input("Type a number!"))
y = int(input("Type an another number!"))

if x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")
else:
    print("x and y are equal!")

    # lesson 2 and
a = int(input("type a number!"))
b = int(input("type a number!"))
c = int(input("type a number!"))

if a >b and c:
    print("a is greater than b and c")
else:
    print("a is not greater than b and c")

    # lesson 3 or
d = int(input("type a number"))
e = int(input("type a number"))
f = int(input("type a number!"))

if d>e or d>f:
    print("d is greater than e or f")
else:
    print("d is not greater than e or f ")

# for not equal

if d ==e and d ==f:
    print("d is equal to e and f") 
else:
    print("de is not equal to e and f")

a = int(input("Your score!"))

if a>=90 and a <= 100:
    print("Grade A")
elif a>=80 and a < 90:
    print("Grade B")
elif a>=60 and a <80:
    print("Grade C")
elif a>= 50 and a < 60:
    print("Grade D")
else:
    print("Fail")

# another way
if  90<=a <= 100:
    print("A")
elif 80<=a <90:
    print("B")
elif 70<=a <80:
    print("C")
elif 60<=a <70:
    print("D")
else:
    print("fail")

def main():
    a = int(input("Type a number!"))
    if even(a):
        print("even")
    else:
        print("odd")

def even(n):
   if n%2 == 0:
       return True 
   else:
       return False
main()

def main():
    a = int(input("type a number!"))
    if even(a):
        print("even")
    else:
        print("odd")
def even(n):
        if n%2 == 0:
            return True
        else:
            return False
main()

def main():
    a = int(input("type a number!"))
    if odd(a):
        print("odd")
    else:
        print("even")

def odd(n):
        if n % 2 != 0:
            return True 
        else:
            return False
main()

def main():
    a = int(input("type a numebr"))
    if odd(a):
        print("odd")
    else:
        print ("even")
def odd(n):
    # if n%2 != 0:
    #    return True
    # else:
    #     return False
    return True if n%2 !=0 else False
main()

# another way
def main():
    a = int(input("type a number"))
    if even(a):
        print("even")
    else:
        print("odd")

def even(n):
    return n% 2 ==0
main()

name = input("Type your name!")
if name =="Harry" or name == "hermonie" or name == "Ron":
    print("Grinffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")

# match case 
name = input("What's your name?")
match name:
    case "app":
        print("hello app")
    case "ec":
        print("hello ec")
    case "zpw":
        print("hello zpw")
    case _:
        print("Who?")


sentence = "hello world"
excited = True

if excited:
    new_sentence = "" 
    for char in sentence:
        new_sentence += char + '!'
    sentence = new_sentence

print(sentence)

sentence = "hello world"
happy = True 

if happy:
    new_ab =""
    for a in sentence:
        new_ab += a + '!'
        sentence = new_ab
print(sentence)

condition = True
print(condition)

condition = False
print(condition)

a = "Hello world!"
b = True

if b:
    new_a =''
    for c in a:
        new_a += c + '!'
    a = new_a
    print(a)

a = "hello world!"
b = False
new_a = ''

for c in a:    
        if b:
            new_a += c
        b = True
print(new_a)

# if and else
condition = True 
condition = False
if condition:
    print("Yes")
else:
    print("No")

print (1+2 ==3)
print(10 * 10 == 200)
print ("a" + "bc" == "ab" + "c")

# opposite 
a= "abcdefg"
opposite_a = ''

for char in a:
    if char =="a":
        print("b")
    if char == "b":
        print("a")
    if char == "c":
        print ("d")
    if char == "d":
        print ("e")
    if char == "e":
        print ("f")
    if char == "f":
        print ("g")
    if char == "g":
        print ("f")
    
opposite_a += char
print(opposite_a)