import requests


class FolderApi:
    def __init__(self, authorization: str) -> None:
        self.authorization = authorization

    def get_folder(self, space_id: str, folder_name: str):
        url = f"https://api.clickup.com/api/v2/space/{space_id}/folder"

        payload = ""
        headers = {"Authorization": self.authorization}

        response = requests.request("GET", url, data=payload, headers=headers)
        folders = response.json()["folders"]
        folder = filter(lambda folder: str(
            folder["name"]).lower() == folder_name.lower(), folders)

        return list(folder)[0]
