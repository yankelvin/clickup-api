import asyncio
import aiohttp
from time import time
from typing import List
from models.Task import Task


class TaskApi:
    def __init__(self, authorization: str) -> None:
        self.authorization = authorization

    async def get_tasks(self, list_id: str) -> List[Task]:
        tasks: List[Task] = []
        page = 0
        finish = False

        urls = []

        while not finish:
            url = f"https://api.clickup.com/api/v2/list/{list_id}/task?subtasks=true&include_closed=true&page={page}"
            headers = {"Authorization": self.authorization}

            urls.append(url)
            page += 1

            if (page + 1) % 5 == 0:
                async with aiohttp.ClientSession(headers=headers, connector=aiohttp.TCPConnector(verify_ssl=False)) as session:
                    response_tasks = await asyncio.gather(*[self.get(url, session) for url in urls])
                urls = []
            else:
                continue

            for response in response_tasks:
                if len(response["tasks"]) == 0:
                    finish = True
                    break
                else:
                    tasks = tasks + response["tasks"]

        return tasks

    async def get(self, url, session):
        try:
            async with session.get(url=url) as response:
                resp = await response.json()
                return resp
        except Exception as e:
            print("Unable to get url {} due to {}.".format(url, e.__class__))
