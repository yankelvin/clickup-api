import requests


class SpaceApi:
    def __init__(self, authorization: str) -> None:
        self.authorization = authorization

    def get_space(self, team_id: str, space_name: str):
        url = f"https://api.clickup.com/api/v2/team/{team_id}/space"

        payload = ""
        headers = {"Authorization": self.authorization}

        response = requests.request("GET", url, data=payload, headers=headers)
        spaces = response.json()["spaces"]
        space = filter(lambda space: str(
            space["name"]).lower() == space_name.lower(), spaces)

        return list(space)[0]
