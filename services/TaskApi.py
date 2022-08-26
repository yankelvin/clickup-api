import requests
from typing import List

from models.Task import Task


class TaskApi:
    def __init__(self, authorization: str) -> None:
        self.authorization = authorization

    def get_tasks(self, list_id: str) -> List[Task]:
        page = 0
        finish = False
        tasks: List[Task] = []

        while not finish:
            url = f"https://api.clickup.com/api/v2/list/{list_id}/task?subtasks=true&include_closed=true&page={page}"
            response_tasks = self.get(url=url)

            if len(response_tasks) == 0:
                finish = True
                break

            tasks = tasks + response_tasks
            page += 1

        return tasks

    def get(self, url):
        headers = {"Authorization": self.authorization}
        response = requests.request(
            "GET", url, data="", headers=headers)
        response_tasks = response.json()["tasks"]

        return response_tasks
