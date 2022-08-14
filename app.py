import os
from flask import Flask, request

from Engine import Engine

authorization = os.environ.get('AUTHORIZATION', None)

app = Flask(__name__)
engine = Engine(authorization=authorization)


@app.route('/', methods=['GET'])
def init():
    return "All Running"


@app.route('/api/get_tasks', methods=['GET'])
def get_tasks():
    try:
        args = request.args
        team_name = args.get("team_name")
        space_name = args.get("space_name")
        folder_name = args.get("folder_name")
        list_name = args.get("list_name")

        tasks = engine.get_tasks(team_name=team_name, space_name=space_name,
                                 folder_name=folder_name, list_name=list_name)

        return tasks
    except Exception as ex:
        return ex


if __name__ == '__main__':
    app.run(debug=True)
