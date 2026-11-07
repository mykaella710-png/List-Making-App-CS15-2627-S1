to_do_list = []
completed_list = []

previous_to_do = []
previous_completed = []
while True:
    choice = input("Choose to:\n1. Add a task\n2. Remove task\n3. Check off to-do\n4. Display to-do list\n5. Display completed list\n6. Undo recent change\n7. Replace existing to-do\n8. Exit \n\nChoice: ")
    if choice == "1":
        previous_to_do = to_do_list.copy()
        previous_completed = completed_list.copy()
        to_do_list.append(input("Task: "))

    elif choice == "2":
        index = 0
        for task in to_do_list:
            print(index, task)
            index = index + 1
        try:
            index = int(input("Enter an index: "))
            task = to_do_list[index]
            previous_to_do = to_do_list.copy()
            previous_completed = completed_list.copy()
            to_do_list.pop(index)
        except IndexError:
            print("Invalid index, please enter an index in the list")
        except ValueError:
            print("Invalid index, please enter a number")

    elif choice == "3":
        index = 0
        for task in to_do_list:
            print(index, task)
            index = index + 1
        try:
            index = int(input("Enter an index: "))
            to_do_list[index]
            previous_to_do = to_do_list.copy()
            previous_completed = completed_list.copy()
            task = to_do_list.pop(index)
            completed_list.append(task)
        except IndexError:
            print("Invalid index, please enter an index in the list")
        except ValueError:
            print("Invalid index, please enter a number")


    elif choice == "4":
        for task in to_do_list:
            print(task)

    elif choice == "5":
        for task in completed_list:
            print(task)

    elif choice == "6":
        to_do_list = previous_to_do.copy()
        completed_list = previous_completed.copy()

    elif choice == "7":
        index = 0
        for task in to_do_list:
            print(index, task)
            index = index + 1
        try:
            index = int(input("Enter an index: "))
            to_do_list[index]
            previous_to_do = to_do_list.copy()
            previous_completed = completed_list.copy()
            new_task = input("Task: ")
            to_do_list[index] = new_task

        except IndexError:
            print("Invalid index, please enter an index in the list")
        except ValueError:
            print("Invalid index, please enter a number")

    elif choice == "8":
        break

    else:
        print("Invalid choice")