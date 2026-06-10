from validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date
)


def add_task(tasks, title, description, due_date):

    if not validate_task_title(title):
        print("Invalid task title.")
        return

    if not validate_task_description(description):
        print("Invalid task description.")
        return

    if not validate_due_date(due_date):
        print("Invalid due date.")
        return

    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }

    tasks.append(task)

    print("Task added successfully!")


def mark_task_as_complete(tasks, task_index):

    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True
        print("Task marked as complete!")
    else:
        print("Invalid task index.")


def view_pending_tasks(tasks):

    pending_tasks = []

    for task in tasks:
        if not task["completed"]:
            pending_tasks.append(task)

    if len(pending_tasks) == 0:
        print("No pending tasks.")
        return

    print("Pending Tasks:")

    for i, task in enumerate(pending_tasks, start=1):
        print(f"{i}. {task['title']}")


def calculate_progress(tasks):

    if len(tasks) == 0:
        return 0

    completed = 0

    for task in tasks:
        if task["completed"]:
            completed += 1

    return (completed / len(tasks)) * 100