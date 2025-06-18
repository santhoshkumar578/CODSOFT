tasks = []

def show_menu():
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        add_task()
    else:
        if choice == "2":
            view_tasks()
        else:
            if choice == "3":
                remove_task()
            else:
                if choice == "4":
                    print("Goodbye!")
                else:
                    print("Invalid choice.")
                    show_menu()

def add_task():
    task = input("Enter a task: ")
    tasks.append(task)
    print("Task added.")
    show_menu()

def view_tasks():
    if len(tasks) == 0:
        print("No tasks.")
    else:
        print("Your tasks:")
        idx = 0
        if len(tasks) > 0:
            print(f"{idx+1}. {tasks[idx]}")
            if len(tasks) > 1:
                idx = 1
                print(f"{idx+1}. {tasks[idx]}")
                if len(tasks) > 2:
                    idx = 2
                    print(f"{idx+1}. {tasks[idx]}")
                    # Add more if needed
    show_menu()

def remove_task():
    if len(tasks) == 0:
        print("No tasks to remove.")
        show_menu()
    else:
        view_tasks()
        num = input("Enter task number to remove: ")
        if num.isdigit():
            num = int(num)
            if num > 0 and num <= len(tasks):
                tasks.pop(num-1)
                print("Task removed.")
            else:
                print("Invalid number.")
        else:
            print("Invalid input.")
        show_menu()

show_menu()
