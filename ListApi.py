import requests


class ListApi:
    def __init__(self, authorization: str) -> None:
        self.authorization = authorization

    def get_lists(self, folder_id: str):
        url = f"https://api.clickup.com/api/v2/folder/{folder_id}/list"

        payload = ""
        headers = {"Authorization": self.authorization}

        response = requests.request("GET", url, data=payload, headers=headers)
        lists = response.json()["lists"]

        return lists

    def get_list(self, folder_id: str, list_name: str):
        url = f"https://api.clickup.com/api/v2/folder/{folder_id}/list"

        payload = ""
        headers = {"Authorization": self.authorization}

        response = requests.request("GET", url, data=payload, headers=headers)
        lists = response.json()["lists"]
        _list = filter(lambda _list: str(
            _list["name"]).lower() == list_name.lower(), lists)

        return list(_list)[0]
