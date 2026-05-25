# exercise day 2 

score = int(input("Type your score!"))
need_score = 50 - score

if 90<=score==100:
    print("Distinction") 
elif 70<=score<=89:
    print("Pass")
elif 50<=score<=69:
    print("Average")
elif 1<=score<50:
    print(f"Fail, You need {need_score} mark to pass")
else:
    print("This is invalid input")