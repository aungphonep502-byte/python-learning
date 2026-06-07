'''# Variable with all 4 data types
a = int(input("Type an integer"))
b = float(input("Type a float"))
c = input("Type a string")
d = (1,2,3,4)
e = {"name" : "app",
     "age" : 23} 
print(a,b,d,e)

# if / elif / else block
a = {"name" : "app",
     "name"  : "zpw"}

b = "app"
for b in a:
    if b in a:
        print("Found")
    elif b not in a:
        print("Not Found")
    else:
        print("INvalid")
        break'''

'''#  while loop with break and continue
b = int(input("type number"))
a = [1,2,3,4,5]
while True:
    
    if b == 3:
        break
    print(b)
    
    #  ✅ List — create, append, remove, slice, enumerate
a = [1,2,3,4,5,6,7]
a.append(9)
print(a)

a.remove(2)
print(a)

print(a[4 :])

for index,b in enumerate(a):
    print(index,b)

    '''
        
'''#  while loop with break and continue
a = 0 
while a < 6:
    a += 1
    if a == 3:
        continue
    print(a)
    

a = 0
while a < 6:
    a += 1
    print(a)
    if a == 3:
        break
    
count = 0

while count < 4:
    print(count)
    count += 1

    a = 0

while a < 5:
    a += 1
    print(a)

    if a == 3:
        break

for i in range(4):
    print(i)
    
for i in range(1, 5):
    print(i)
for i in range(1, 6, 2):
    print(i)
x = 10

if x > 5:
    print("A")
else:
    print("B")
    x = 3

if x > 5:
    print("A")
else:
    print("B")
def add(a, b):
    return a + b

print(add(2, 3))
def greet():
    print("Hello")

greet()

x = 3

if x > 5:
    print("A")
else:
    print("B")

numbers = [10, 20, 30]

for n in numbers:
    print(n)

count = 0

while count < 4:
    print(count)
    count += 1
'''  


















    
