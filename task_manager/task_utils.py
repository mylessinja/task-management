import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from validation import (
    validate_title,
    validate_description,
    validate_due_date,
)


def add_task(tasks, title, description, due_date):
    validate_title(title)
    validate_description(description)
    validate_due_date(due_date)

    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False,
    }
    tasks.append(task)
    print("Task added successfully!")


def mark_complete(tasks, task_index):
    if task_index < 1 or task_index > len(tasks):
        raise ValueError("Invalid task index.")
    tasks[task_index - 1]["completed"] = True
    print("Task marked as complete!")


def view_pending_tasks(tasks):
    pending = [t for t in tasks if not t["completed"]]
    if len(pending) == 0:
        return
    for task in pending:
        print(f"Title: {task['title']}")
        print(f"Description: {task['description']}")
        print(f"Due Date: {task['due_date']}")
        print()


def calculate_progress(tasks):
    if len(tasks) == 0:
        return 0.0
    completed = sum(1 for t in tasks if t["completed"])
    progress = (completed / len(tasks)) * 100
    print(progress)
    return progress
