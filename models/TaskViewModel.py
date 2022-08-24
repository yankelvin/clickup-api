from datetime import datetime


class TaskViewModel:
    task_id: str
    task_name: str
    status: str
    assignee: str
    due_date: str
    start_date: str
    date_created: str
    date_closed: str
    list_name: str
    points: int
    category_name: str
    parent_id: str

    def __init__(self, task_id: str,
                 task_name: str,
                 status: str,
                 assignee: str,
                 due_date: str,
                 start_date: str,
                 date_created: str,
                 date_closed: str,
                 list_name: str,
                 points: int,
                 category_name: str,
                 parent_id: str) -> None:
        self.task_id = task_id
        self.task_name = task_name
        self.status = status
        self.assignee = assignee
        self.list_name = list_name
        self.points = points
        self.category_name = category_name
        self.parent_id = parent_id

        self.due_date = None if due_date is None else datetime.fromtimestamp(
            int(due_date) / 1000).strftime("%d/%m/%Y - %H:%M:%S")
        self.start_date = None if start_date is None else datetime.fromtimestamp(
            int(start_date) / 1000).strftime("%d/%m/%Y - %H:%M:%S")
        self.date_created = None if date_created is None else datetime.fromtimestamp(
            int(date_created) / 1000).strftime("%d/%m/%Y - %H:%M:%S")
        self.date_closed = None if date_closed is None else datetime.fromtimestamp(
            int(date_closed) / 1000).strftime("%d/%m/%Y - %H:%M:%S")
