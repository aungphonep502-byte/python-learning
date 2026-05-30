# guessing game
import random 
a = random.randint(1,10)
guess =7

while guess >1:
    b = int(input("guess a number!"))  
    if b > a:
        print("high")
    elif b < a:
        print("low")
    else:
        print("correct")
        break

    guess -= 1
    print ("guess left:", guess)

    if guess ==0:
        print("game over!")

import random 
a = random.randint(1,10)
guess = 7

while guess >1:
    b = int(input("guess a number"))
    if b > a:
        print("high")
    elif b < a:
        print("low")
    else:
        print("Correct")
        break 
    guess -= 1 
    print (f"guess time left,{guess}")

    if guess == 0:
        print("Game over")
c= 0
b = int(input("type a number"))
for a in range(1,11):
    c = b * a
    print(c)

import random 
a = random.randint(1,10)
guess = 5

while guess >0:
    b = int(input("type a number"))
    if b > a:
        print("high")
    elif b < a:
        print("low")
    else :
        print("correct!")
        break
    guess -= 1
    print ("guess left", guess)
    if guess == 0:
     print("Game over")

# list
a = ["app", "zpw", "acm"]
a.insert(1,"lulu")
print(a)
a.append("lulu")
print (a)
a.remove("app")
print(a)

a.pop(1)
print(a)
print(len(a))

a = ["pizza","burger",'rice']
a.remove("burger")
a.insert(1,"rice")
a.pop(2)
a.insert(2,"noodle")
print(a)

a = ["apple","banana","grape"]
# a.remove("banana")
# a.pop(2)
a.insert(1,"app")
a.append("lulu")
print (len(a))

a =["zpw","lulu","app"]
a= [9,2,37,34]
print(a[0:])
print(a[:])
for index,b in enumerate(a):
    print(index,b)
for index,b in enumerate(a):
    print (index,b)
a.sort()
print(a)

a = ["car","home","phone","people","abd"]
for index,b in enumerate(a):
    print(index,b)
a.sort()
print(a)

new_a = sorted(a)
print(a)
print(new_a)

names =["John","Mike","Anna","David"]
print(names[:2])

for name in names:
    print(name)

names.sort()
print(names)

names.reverse()
print(names)

if "John" in names:
    print("Found")
else:
    print("not found")

color = ("red","blue","green")
color[0] = "purple"
print(color)

color = ["red","blue","green"]
# for index, new_color in enumerate(color):
#     print(index, new_color)

new_color= sorted(color)
print(new_color)
print(color)

cities = ["Yangon", "Mandalay", "Naypyitaw", "Mawlamyine", "Taunggyi"]
largest = ""
for city in cities:
    if len(city) > len(largest):
       largest = city
print(largest)


cities = ["Yangon", "Mandalay", "Naypyitaw", "Mawlamyine", "Taunggyi"]
count = ""

for city in cities:
    if city == 1:
        count = city
print(count)

count = len(cities)
print(count)

# Create a List of 5 Myanmar Cities
cities = ["Yangon","Mandalay","Naypyitaw","Taunggyi","Mawlamyine"]
for city in cities:
    print (city)
cities.append("Inlay")
cities.insert(2,"Inlay")
cities.pop(2)
cities.remove("Taunggyi")
cities.sort()
city = sorted(cities)
print(city)

# 5. Find the Longest City Name Using a Loop
longest =""
for city in cities:
    if len(city) > len(longest):
        longest = city
print(f"longest city is {longest}")

print(cities[: 3])