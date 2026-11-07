shopping_list = []
previous_list = []
while True:
    choice = input("Choose to:\n1. Add an item\n2. Remove item\n3. Display list\n4. Undo recent change\n5. Exit\n\nChoice: ")
    if choice == "1":
        previous_list = shopping_list.copy()
        shopping_list.append(input("Item:"))
    elif choice == "2":
        index = 0
        for item in shopping_list:
            print(index, item)
            index = index + 1

        index = int(input("Enter an index: "))
        previous_list = shopping_list.copy()
        item = shopping_list.pop(index)

    elif choice == "3":
        for task in shopping_list:
            print (task)
    elif choice == "4":
        shopping_list = previous_list.copy()
    elif choice == "5":
        break
