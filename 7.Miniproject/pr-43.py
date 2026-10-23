
tasks = []

def add_task():
    task = input("Enter your task: ").strip()

    if task == "":
        print("Task cannot be empty!")
    else:
        tasks.append(task)
        print("Task added successfully!")

def view_tasks():
    if len(tasks) == 0:
        print("Your to-do list is empty!")
    else:
        print("\n===== YOUR TO-DO LIST =====")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def remove_task():
    view_tasks()

    if len(tasks) == 0:
        return

    try:
        number = int(input("Enter task number to remove: "))

        if 1 <= number <= len(tasks):
            removed = tasks.pop(number - 1)
            print(f"Removed task: {removed}")
        else:
            print("Invalid task number!")

    except ValueError:
        print("Please enter a valid number!")

while True:
    print("\n===== TO-DO LIST MENU =====")
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Goodbye! Keep completing your tasks.")
        break
    else:
        print("Invalid choice! Please select 1-4.")
