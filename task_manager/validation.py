def validate_title(title):
    if not isinstance(title, str) or len(title) == 0:
        raise ValueError("Title cannot be empty.")
    return title


def validate_description(description):
    if not isinstance(description, str) or len(description) == 0:
        raise ValueError("Description cannot be empty.")
    return description


def validate_due_date(due_date):
    if not isinstance(due_date, str) or len(due_date) == 0:
        raise ValueError("Due date cannot be empty.")
    parts = due_date.split("-")
    if len(parts) != 3:
        raise ValueError("Due date must be in YYYY-MM-DD format.")
    return due_date
