#to do list
tasks = []

#function to add tasks
def add_task():
    task = input("Enter your task")
    tasks.append({"Task":task, "Status":"pending"})
    print("New Task Successfully Added!")
    print("\n")


#function to view tasks
def view_task():
    if not tasks:
        print("No Tasks Found")
    else:
        print("Your Tasks are:")
        for index,todo in enumerate(tasks,1):
            print(f"{index} : {todo['Task']} - {todo['Status']}")
    print("\n")


#function to remove tasks
def remove_task():
    if not tasks:
        print("No Tasks Found\n")
    else:
        try:
            search_index = int(input("Enter the task number to be deleted:"))-1
            if 0 <= search_index < len(tasks):
                removed_task = tasks.pop(search_index)
                print(f"Removed Task: {removed_task['Task']}")
            else:
                print("Invalid Task Number\n")
        except ValueError as e:
            print("Please enter a valid task number")
        print("\n")


#function to mark a task as completed
def mark_as_completed():
    if not tasks:
        print("No Tasks Found\n")
    else:
        try:
            search_index = int(input("Enter the task number to be mark as completed:"))-1
            if 0 <= search_index < len(tasks):
                tasks[search_index]['Status'] ='done'
                print(f"{tasks[search_index]['Task']} has been marked as done.")
            else:
                print("Invalid Task Number\n")
        except ValueError as e:
            print("Please enter a valid task number")
        print("\n")


while True:
    print("---- TO DO LIST ----")
    print("1. Add a New Task")
    print("2. View All Tasks")
    print("3. Remove a Task")
    print("4. Mark a Task as Completed")
    print("5. Exit")

    choice = input("Enter Your Choice").strip()

    if choice == "1":
        add_task()
    elif choice == "2":
        view_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        mark_as_completed()
    elif choice == "5":
        print("Exiting...")
        exit()
    else:
        print("Invalid Input")
