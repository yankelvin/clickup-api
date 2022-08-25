from time import time
from typing import List
from datetime import datetime, timedelta

from models.Task import CustomField, Task
from models.TaskDTO import TaskDTO

from services.TeamApi import TeamApi
from services.SpaceApi import SpaceApi
from services.FolderApi import FolderApi
from services.ListApi import ListApi
from services.TaskApi import TaskApi


class Engine:
    def __init__(self, authorization: str) -> None:
        self.authorization = authorization
        self.team_api = TeamApi(self.authorization)
        self.space_api = SpaceApi(self.authorization)
        self.folder_api = FolderApi(self.authorization)
        self.list_api = ListApi(self.authorization)
        self.task_api = TaskApi(self.authorization)

        self.cache = {
            "ttl": datetime.now(),
            "team_id": None,
            "space_id": None,
            "folder_id": None
        }

    def get_cache_value(self, value_name: str):
        if (self.cache["ttl"] + timedelta(minutes=30)) > datetime.now():
            return self.cache[value_name]
        return None

    def set_cache_value(self, value_name: str, value: str):
        self.cache[value_name] = value
        
    def get_lists(self, team_name: str, space_name: str, folder_name: str):
        team_id = self.__get_team_id(team_name)
        space_id = self.__get_space_id(space_name, team_id)
        folder_id = self.__get_folder_id(folder_name, space_id)
        lists = self.list_api.get_lists(folder_id=folder_id)
        
        return lists

    def get_tasks(self, team_name: str, space_name: str, folder_name: str, list_name: str, page: int):
        start_time = time()

        team_id = self.__get_team_id(team_name)
        space_id = self.__get_space_id(space_name, team_id)
        folder_id = self.__get_folder_id(folder_name, space_id)

        print(f"Obter Folder --- {(time() - start_time):2f} seconds ---")

        tasks = []

        if list_name is None:
            tasks = self.__get_all_tasks_by_folder(folder_id, tasks, page)
        else:
            tasks = self.__get_all_tasks_by_list(list_name, folder_id, tasks, page)

        print(f"Fim --- {(time() - start_time):2f} seconds ---")
        return tasks

    def __get_all_tasks_by_folder(self, folder_id, tasks, page):
        start_time = time()
        lists = self.list_api.get_lists(folder_id=folder_id)
        print(f"Obter Listas --- {(time() - start_time):2f} seconds ---")
        for _list in lists:
            start_time = time()
            list_tasks = self.task_api.get_tasks(list_id=_list["id"], page=page)
            print(
                f"Obter Tasks - Lista: {_list['id']} --- {(time() - start_time):2f} seconds ---")

            start_time = time()
            tasks = tasks + self.__map_tasks(list_tasks)
            print(f"Mapear Tasks --- {(time() - start_time):2f} seconds ---")

        return tasks

    def __get_all_tasks_by_list(self, list_name, folder_id, tasks, page):
        start_time = time()
        _list = self.list_api.get_list(
            folder_id=folder_id, list_name=list_name)
        list_id = _list["id"]
        print(f"Obter Lista --- {(time() - start_time):2f} seconds ---")

        start_time = time()
        list_tasks = self.task_api.get_tasks(list_id=list_id, page=page)
        print(
            f"Obter Tasks - Lista: {_list['id']} --- {(time() - start_time):2f} seconds ---")

        start_time = time()
        tasks = tasks + self.__map_tasks(list_tasks)
        print(f"Mapear Tasks --- {(time() - start_time):2f} seconds ---")

        return tasks

    def __map_tasks(self, tasks: List[Task]):
        task_dtos = []

        for task in tasks:
            task_dto = self.__create_dto(task)
            task_dtos.append(task_dto)

        return task_dtos

    def __create_dto(self, task: Task):
        assignee_names = self.__get_assignee_names(task)
        category_name = self.__get_category_name(task)

        task_dto = TaskDTO(task["id"], task["name"], task["status"]["status"], assignee_names, task["due_date"], task["start_date"],
                           task["date_created"], task["date_updated"], task["date_closed"], task["list"]["name"], task["points"], category_name, task["parent"])

        return task_dto.__dict__

    def __get_assignee_names(self, task: Task):
        assignees = [creator["username"] for creator in task["assignees"]]
        assignee_name = ", ".join(assignees)
        return assignee_name

    def __get_category_name(self, task: Task):
        category: CustomField = list(filter(
            lambda field: field["name"] == "CATEGORIA", task["custom_fields"]))[0]

        category_name = ""

        if "value" in category:
            category_name = list(filter(
                lambda option: option["orderindex"] == category["value"], category["type_config"]["options"]))[0]["name"]

        return category_name

    def __get_folder_id(self, folder_name, space_id):
        folder_id = self.get_cache_value("folder_id")

        if folder_id is None:
            folder = self.folder_api.get_folder(
                space_id=space_id, folder_name=folder_name)
            folder_id = folder["id"]
            self.set_cache_value("folder_id", folder_id)
        return folder_id

    def __get_space_id(self, space_name, team_id):
        space_id = self.get_cache_value("space_id")

        if space_id is None:
            space = self.space_api.get_space(
                team_id=team_id, space_name=space_name)
            space_id = space["id"]
            self.set_cache_value("space_id", space_id)
        return space_id

    def __get_team_id(self, team_name):
        team_id = self.get_cache_value("team_id")

        if team_id is None:
            team = self.team_api.get_team(team_name=team_name)
            team_id = team["id"]
            self.set_cache_value("team_id", team_id)

        return team_id
