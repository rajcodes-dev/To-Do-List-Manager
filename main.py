import json

file_name = "to_do_list.json"


def load_task():
    try:
        with open(file_name, "r") as file:
            return json.load(file)    
    except:
        return {"tasks": []}


def save_task(tasks):
    try:
        with open(file_name, "w") as file:
            json.dump(tasks, file)
    except:
        print("Failed to save.")


def view_task():
    pass


def create_task(tasks):
    description = input("Enter task description: ").strip()
    if description:
        tasks["tasks"].append({"Description": description, "Complete": False})
        save_task(tasks)
        print("Task Added.")
    else:
        print("Description cannot be empty.")


def mark_task_complete():
    pass


def main():
    tasks = load_task()
    print(tasks)

    while True:
        print("\nTo-Do List Manager")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_task()

        elif choice == "2":
            create_task()

        elif choice == "3":
            mark_task_complete()

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid Choice. Try again.")


main()
