# student scores and names CRUD project
students = {}
while True:
    print("1 — Add student (name + score)") 
    print("2 — View all students and scores") 
    print("3 — Find highest scoring student")
    print("4 — Find lowest scoring student")
    print("5 — Calculate class average")
    print("6 — Remove a student by name")
    print("7 — Quit")
   
    option = input("Choice your Option!")
    if option == "1":
        name = input("Add your name!")
        score = int(input("Add your score!"))
        students[name] = score
        print("Your name is",name,"Your score is",score)
    elif option == "2":
        if not students:
            print("Empty")
        else:
            for name, score in students.items():
                print('all students and score', name, "-", score)
    elif option == "3":
        max_student = max(students, key = students.get)
        print(" highest scoring student is","-",max_student, students[max_student])
    elif option == "4":
        low_student = min(students, key=students.get)
        print("lowest scoring student is", "-", low_student, students[low_student])
    elif option =="5":
        average = sum(students.values()) / len(students)
        print("class average is", average)
    elif option == "6":
        name = input("Type a name to remove a student by name")
        if not students:
            print("Removed name not found")
        else:
            del students[name]
            print("Removed name")
    elif option == "7":
        print("Quit")
        break
    else:
        print("Invalid input")



       