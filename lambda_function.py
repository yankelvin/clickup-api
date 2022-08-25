import os
from services.Engine import Engine

authorization = os.environ.get('AUTHORIZATION', None)
engine = Engine(authorization=authorization)


async def lambda_handler(event, context):
    try:
        print(event)
        
        query = event["query"]
        team_name = query["team_name"]
        space_name = query["space_name"]
        folder_name = query["folder_name"]
        list_name = query["list_name"]

        tasks = await engine.get_tasks(team_name=team_name, space_name=space_name,
                                       folder_name=folder_name, list_name=list_name)

        return tasks
    except Exception as ex:
        return ex

