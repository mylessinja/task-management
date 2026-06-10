def validate_task_title(title):
    return len(title.strip()) > 0


def validate_task_description(description):
    return len(description.strip()) > 0


def validate_due_date(due_date):
    return len(due_date.strip()) > 0