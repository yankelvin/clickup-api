from flask import Flask, request
from pprint import pprint

from Engine import Engine

authorization = "pk_6381265_FIKH47ASHJZ43DPAPEVBNVLRV30ZQXT7"

app = Flask(__name__)
engine = Engine(authorization=authorization)


@app.route('/get_tasks', methods=['GET'])
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
