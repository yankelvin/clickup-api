import os
from services.Engine import Engine
from services.MongoDB import MongoDB

authorization = os.environ.get('AUTHORIZATION', None)
connectionString = os.environ.get('CONNECTION_STRING', None)

team_name = os.environ.get('TEAM_NAME', None)
space_name = os.environ.get('SPACE_NAME', None)
folder_name = os.environ.get('FOLDER_NAME', None)

engine = Engine(authorization=authorization)
mongodb = MongoDB(connectionString=connectionString)


def lambda_handler(event, context):
    try:
        tasks = engine.get_tasks(team_name=team_name, space_name=space_name,
                                 folder_name=folder_name, list_name=None)

        mongodb.delete_all_tasks()
        mongodb.insert_tasks(tasks)

        return f"Tasks inseridas: {len(tasks)}"
    except Exception as ex:
        print(ex)
        return ex
