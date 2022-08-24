import requests
from typing import List
from models.Task import Task


class TaskApi:
    def __init__(self, authorization: str) -> None:
        self.authorization = authorization

    def get_tasks(self, list_id: str) -> List[Task]:
        tasks: List[Task] = []
        page = 0

        while True:
            url = f"https://api.clickup.com/api/v2/list/{list_id}/task?subtasks=true&page={page}"

            payload = ""
            headers = {"Authorization": self.authorization}

            response = requests.request(
                "GET", url, data=payload, headers=headers)
            response_tasks = response.json()["tasks"]

            if len(response_tasks) == 0:
                break

            tasks = tasks + response_tasks
            page += 1

        return tasks
