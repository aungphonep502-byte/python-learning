 Phones = ["Samsung", "Apple", "oppo", "Xiaomi","Vivo"]
# Access first and last item using index and negative index
# print(Phones[0])
# print(Phones[-1])

# Add an item with .append(), remove one with .remove()
Phones.append("Pixel")
Phones.remove("Samsung")
print(Phones)

# Loop through the list using enumerate()
for index, Phone in enumerate(Phones,start=1):
    print(index,"-",Phone)

# Slice the list to get the first 3 items
print(Phones[: 3])


# day 5 lessons dic
# create a dictionary
student = {
    "name" : "Andrew",
    "age"  : 23,
    "address" : "NorthOkkalapa"} 
print(student)
# access value
print(student["address"])
print(student["name"])

# .get() function
# error
# print(student["email"]) 
# solve with get function
print(student.get("email","Not Found"))

# Add a New Key
student ["Sign"] = "drew"
print(student)

# update a value
student ["name"] = "Drew"
print(student) 

# delete a key
del student ["name"]
print(student)
student.pop("Sign")
print(student)

# Check if a Key Exists
if 'address' in student:
    print("found!")
print("age" in student)


# mini practice
sneaker = {"brand" : "Nike",
           "model" : "Airforce 1",
           "color" : "white"}

print (sneaker["model"])

sneaker["price"] = "150 dollar"
print(sneaker)

sneaker["color"] = "Black"
print(sneaker)

del sneaker["price"]
print(sneaker)

if "brand" in sneaker:
    print("Found")

print(sneaker.get("size", "Not found"))


# function keys.()
student ={
    "name" : "Drew",
    "age"  : 23,
    "country"  : "Myanmar"
}
for key in student.keys():
    print(key)

# function values.()
for value in student.values():
    print(value)

# items.()
for item in student.items():
    print(item)

# keys and values
for key, value in student.items():
    print(key, value)

# nested dictionary
people = {
    "person1" : {
        "name" : "Drew",
        "age" : 23
    },
        "person2" : {
        "name" : "app",
        "age"  : 24
    }
}
# print(people["person1"]["name"])
for person, info in people.items():
    print(person)

    for key, value in info.items():
        print(key,value)

# create a set
fruits = {"apple", "banana", "grape"}
print(fruits)
fruits.add("strawberry")
print(fruits)
fruits.remove("apple")
print(fruits)

# set operation
set1 = {1,2,3,4}
set2 = {3,4,5,6}
# union
print(set1 | set2)
print(set1.union(set2))

# intersection
print(set1 & set2)
print(set1.intersection(set2))

# challenge
students = {
    "student1": {
        "name" : "Aung",
        "age"  : 20
    },
    "student2" : {
        "name" : 'Alex',
        "age"  : "22"
    }
}
print(students["student1"]["name"])
print(students["student2"] ["age"])

for student,info in students.items():
    print(student)
    for key, value in info.items():
        print(key,value)

# create a set
create_set = {1,1,2,2,3,3} 
create_set.add(4)
print(create_set)
create_set.remove(2)
print(create_set)

# union
a = {1,2,3} 
b = {3,4,5}
print(a|b)
print(a.union(b))
print(a.intersection(b))
print(a & b)

student = {
    "name" : "Aung",
    "age"  : 23,
    "city"  : "Yangon",
    "is_student" : True
}
for key, value in student.items():
    print(key,value)

students = {
    "student1": {
        "name" : "Aung",
        "score" :85
    },
    "student2": {
        "name" : "Alex",
        "score" :92
    },
    "student3": {
        "name" : "john",
        "score" : 78
    }
}
# for student,info in students.items():
#     print(student)
#     for key,value in info.items():
#         print(key,value)
# highest_score = 0
# student_name = ""
# for student,info in students.items():
#     if info["score"] > highest_score :
#         highest_score = info["score"]
#         student_name = info["name"]
# print(student_name, highest_score)

remove_set = [1,1,2,2,3,3]
remove_duplicate = list(set(remove_set))
print(remove_duplicate)

fruits = ["apple",
          "banana",
          "banana",
          "strawberry",
          "apple",
          "strawberry",
          "banana"]

count = {} 
for fruit in fruits:
    if fruit in count:
        count[fruit] += 1
    else:
        count[fruit] = 1
for fruit2, total in count.items():
     print(fruit2,total)


        
