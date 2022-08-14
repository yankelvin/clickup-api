import requests


class TeamApi:
    def __init__(self, authorization: str) -> None:
        self.authorization = authorization

    def get_team(self, team_name: str):
        url = "https://api.clickup.com/api/v2/team"

        payload = ""
        headers = {"Authorization": self.authorization}

        response = requests.request("GET", url, data=payload, headers=headers)
        teams = response.json()["teams"]
        team = filter(lambda team: str(
            team["name"]).lower() == team_name.lower(), teams)

        return list(team)[0]
