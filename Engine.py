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

    def get_tasks(self, team_name: str, space_name: str, folder_name: str, list_name):
        team = self.team_api.get_team(team_name=team_name)
        team_id = team["id"]

        space = self.space_api.get_space(
            team_id=team_id, space_name=space_name)
        space_id = space["id"]

        folder = self.folder_api.get_folder(
            space_id=space_id, folder_name=folder_name)
        folder_id = folder["id"]

        tasks = []

        if list_name is None:
            lists = self.list_api.get_lists(folder_id=folder_id)
            for _list in lists:
                list_tasks = self.task_api.get_tasks(list_id=_list["id"])
                tasks = tasks + \
                    [{"list_name": _list["name"], "tasks": list_tasks}]

        else:
            _list = self.list_api.get_list(
                folder_id=folder_id, list_name=list_name)
            list_id = _list["id"]

            tasks = tasks + self.task_api.get_tasks(list_id=list_id)

        return tasks
