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
    parent_name: str

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
                 parent_id: str,
                 parent_name: str) -> None:
        self.task_id = task_id
        self.task_name = task_name
        self.status = status
        self.assignee = assignee
        self.due_date = due_date
        self.start_date = start_date
        self.date_created = date_created
        self.date_closed = date_closed
        self.list_name = list_name
        self.points = points
        self.category_name = category_name
        self.parent_id = parent_id
        self.parent_name = parent_name
