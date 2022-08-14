from datetime import datetime, timedelta

from TeamApi import TeamApi
from SpaceApi import SpaceApi
from FolderApi import FolderApi
from ListApi import ListApi
from TaskApi import TaskApi


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

    def get_tasks(self, team_name: str, space_name: str, folder_name: str, list_name):
        team_id = self.__get_team_id(team_name)
        space_id = self.__get_space_id(space_name, team_id)
        folder_id = self.__get_folder_id(folder_name, space_id)

        tasks = []

        if list_name is None:
            tasks = self.__get_all_tasks_by_folder(folder_id, tasks)
        else:
            tasks = self.__get_all_tasks_by_list(list_name, folder_id, tasks)

        return tasks

    def __get_all_tasks_by_list(self, list_name, folder_id, tasks):
        _list = self.list_api.get_list(
            folder_id=folder_id, list_name=list_name)
        list_id = _list["id"]

        tasks = tasks + self.task_api.get_tasks(list_id=list_id)
        return tasks

    def __get_all_tasks_by_folder(self, folder_id, tasks):
        lists = self.list_api.get_lists(folder_id=folder_id)
        for _list in lists:
            list_tasks = self.task_api.get_tasks(list_id=_list["id"])
            tasks = tasks + \
                [{"list_name": _list["name"], "tasks": list_tasks}]

        return tasks

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
