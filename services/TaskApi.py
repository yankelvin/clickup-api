import requests


class TaskApi:
    def __init__(self, authorization: str) -> None:
        self.authorization = authorization

    def get_tasks(self, list_id: str):
        url = f"https://api.clickup.com/api/v2/list/{list_id}/task"

        payload = ""
        headers = {"Authorization": self.authorization}

        response = requests.request("GET", url, data=payload, headers=headers)
        tasks = response.json()["tasks"]

        return tasks
