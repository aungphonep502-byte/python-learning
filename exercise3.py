a = 3
for b in range(1,11):
    result = b * a
    print (f"{b }*{a} = {result}")

import random
number = random.randint(1,100)
print(number)

import random 
a = random.randint(1,100)
print (a)

import random
a = random.randint(1,100)
print (a)

import random 
a = random.randint(1,100)
print (a)

import random 
a = random.randint(1,10)
while True:
    b = int(input("type a number!"))
    
    if b > a:
        print ("high")
    elif b <a:
        print("low")
    elif b == a:
        print("Correct!")
        break
    else:
        print("what?")
        

import random 
a = random.randint(1,10)

guess = 7
while guess > 0:
    b = int(input("guess a number!"))
    if b > a:
        print ("High")
    elif b < a:
        print ("low")
    else:
        print ("Correct")
        break
    guess -= 1
    print("guesses left", guess)
if guess ==0:
    print(f" your guess is{guess} over")

import random 
a = random.randint(1,10)
guess = 7

while True:
    guess > 0
    b =int(input("type a number"))
    if b > a:
        print("high")
    elif b < a:
        print ("low")
    else:
        print("correst")
        break 
    guess -= 1
    print("guess time:", guess)

if guess == 0:
    print("Game Over")

import random 
a = random.randint(1,10)

for guess in range(7):
    b = int(input("type a number"))
    if b > a:
        print("high")
    elif b < a:
        print("low")
    else :
        print("Correct")
        break
   
    print("guess time left", 6 - guess)

if guess == 0:
    print("Game over")

b= int(input("type a number!"))
for a in range(1,11):
    x = b * a
    print(x)

a = int(input("type a number"))
for x in range(1,11):
    b = a * x
    print(f"{a}*{x}={b}")
    
import random
a=  random.randint(1,10)
guess = 7

while guess >0:
    b = int(input("type a number"))
    if b >10:
        print("hight")
    elif b < 10:
        print("low")
    else:
        print("correct")
        break
    guess -= 1
    print("guess time left", guess)

    if guess ==0:
        print("Game over!")
    

