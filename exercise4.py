# shopping list project
shopping_list = []

while True:
    print("\n===== Shopping List Menu =====")
    print("1 — Add item to list")
    print("2 — Remove item from list")
    print("3 — View all items")
    print("4 — Check if an item is in the list")
    print("5 — Clear the entire list")
    print("6 — Quit")

    choose = input("Choose your option")
    if choose == "1":
        item = input("Add item")
        shopping_list.append(item)
        print("added your item",item)
        print("total amount : ",len(shopping_list))

    elif choose =="2":
        item = input("Type data to remove")
        if item in shopping_list:
            shopping_list.remove(item)
            print("Data already removed",shopping_list)
            print("total amount : ",len(shopping_list)) 
        else:
            print("data not found")
    
    elif choose == "3":
        if len(shopping_list) ==0:
            print("empty")
        else:
            sorted_list = sorted(shopping_list)
            for index, item in enumerate(sorted_list, start= 1):
                print(index,"-",item)
            print("total amount : ",len(shopping_list)) 
    
    elif choose == "4":
        item = input("Type an item to find in the list")
        if item in shopping_list:
            print("Avaliable")
            print("total amount : ",len(shopping_list)) 
        else:
            print("Not avaliable")
    
    elif choose =="5":
        shopping_list.clear()
        print("Clear the list")

    elif choose == "6":
        print("Quit")
        print("total amount : ",len(shopping_list))
        break

    else:
        print("Invalid data")


   
        


        



