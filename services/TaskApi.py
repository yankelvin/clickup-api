import requests
from time import time
from typing import List
from models.Task import Task


class TaskApi:
    def __init__(self, authorization: str) -> None:
        self.authorization = authorization

    def get_tasks(self, list_id: str, page: int) -> List[Task]:
        tasks: List[Task] = []

        url = f"https://api.clickup.com/api/v2/list/{list_id}/task?subtasks=true&include_closed=true&page={page}"
        headers = {"Authorization": self.authorization}

        start_time = time()

        response = self.__send_request(url, "", headers)
        tasks = tasks + response
        
        print(f"Url: {url} --- {(time() - start_time):2f} seconds ---")

        return tasks

    def __send_request(self, url, payload, headers):
        response = requests.request(
            "GET", url, data=payload, headers=headers)
        response_tasks = response.json()["tasks"]
        return response_tasks
