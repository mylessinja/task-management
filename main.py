import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "task_manager"))

from task_utils import (
    add_task,
    mark_complete,
    view_pending_tasks,
    calculate_progress,
)

tasks = []


def main():
    while True:
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. Calculate Progress")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            title = input("Enter task title: ").strip()
            description = input("Enter task description: ").strip()
            due_date = input("Enter due date (YYYY-MM-DD): ").strip()
            add_task(tasks, title, description, due_date)

        elif choice == "2":
            view_pending_tasks(tasks)
            task_index = int(input("Enter task number to mark complete: ").strip())
            mark_complete(tasks, task_index)

        elif choice == "3":
            view_pending_tasks(tasks)

        elif choice == "4":
            calculate_progress(tasks)

        elif choice == "5":
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
