from task_utils import (
    add_task,
    mark_task_as_complete,
    view_pending_tasks,
    calculate_progress
)

tasks = []

while True:

    print("1. Add Task")
    print("2. Mark Task as Complete")
    print("3. View Pending Tasks")
    print("4. Check Progress")
    print("5. Exit")

    choice = input()

    if choice == "1":

        title = input()
        description = input()
        due_date = input()

        add_task(tasks, title, description, due_date)

    elif choice == "2":

        try:
            task_number = int(input())
            mark_task_as_complete(tasks, task_number - 1)
        except ValueError:
            print("Invalid input.")

    elif choice == "3":

        view_pending_tasks(tasks)

    elif choice == "4":

        progress = calculate_progress(tasks)
        print(f"{progress:.2f}%")

    elif choice == "5":

        break

    else:
        print("Invalid choice.")