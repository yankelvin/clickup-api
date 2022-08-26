import json
import os
import asyncio
from services.Engine import Engine

authorization = os.environ.get('AUTHORIZATION', None)
engine = Engine(authorization=authorization)

loop = asyncio.get_event_loop()


def lambda_handler(event, context):
    try:
        print(event)

        query = event["queryStringParameters"]
        team_name = query["team_name"]
        space_name = query["space_name"]
        folder_name = query["folder_name"]
        list_name = None
        
        if "list_name" in query:
            list_name = query["list_name"]

        tasks = loop.run_until_complete(engine.get_tasks(team_name=team_name, space_name=space_name,
                                                         folder_name=folder_name, list_name=list_name))

        return {
            "statusCode": 200,
            "headers": {},
            "body": json.dumps(tasks)
        }
    except Exception as ex:
        print(ex)
        return ex
