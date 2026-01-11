import json

file_name = "to_do_list.json"

# to be added: 1. marked as incomplete  2. delete task


def load_task():
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except:
        return {"tasks": []}


def save_task(tasks):
    try:
        with open(file_name, "w") as file:
            json.dump(tasks, file, indent=4)
    except:
        print("Failed to save.")


def view_task(tasks):
    print()
    task_list = tasks["tasks"]
    if len(task_list) == 0:
        print("No task to display.")
    else:
        print("Your To-Do List: ")
        for idx, task in enumerate(task_list):
            if task["complete"]:
                status = "[Completed]"
            elif task["incomplete"]:
                status = "[Incompleted]"
            else:
                status = "[Pending]"
            print(f"{idx+1}. {task['description']} | {status}")


def create_task(tasks):
    description = input("Enter task description: ").strip()
    if description:
        tasks["tasks"].append(
            {"description": description, "complete": False, "incomplete": False}
        )
        save_task(tasks)
        print("Task Added.")
    else:
        print("Description cannot be empty.")


def mark_task_complete(tasks):
    view_task(tasks)
    try:
        task_number = int(input("Enter the task number to mark as complete: ").strip())
        if 1 <= task_number <= len(tasks["tasks"]):
            tasks["tasks"][task_number - 1]["complete"] = True
            tasks["tasks"][task_number - 1]["incomplete"] = False
            save_task(tasks)
            print("Marked as complete")
        else:
            print("Invalid task number.")
    except:
        print("Enter the valid number.")


def mark_task_incomplete(tasks):
    view_task(tasks)
    try:
        task_number = int(
            input("Enter the task number to mark as incomplete: ").strip()
        )
        if 1 <= task_number <= len(tasks["tasks"]):
            tasks["tasks"][task_number - 1]["complete"] = False
            tasks["tasks"][task_number - 1]["incomplete"] = True
            save_task(tasks)
            print("Marked as incomplete")
    except:
        print("Enter the valid number.")


def main():
    tasks = load_task()

    while True:
        print("\nTo-Do List Manager")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Incomplete Task")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_task(tasks)

        elif choice == "2":
            create_task(tasks)

        elif choice == "3":
            mark_task_complete(tasks)

        elif choice == "4":
            mark_task_incomplete(tasks)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid Choice. Try again.")


main()
