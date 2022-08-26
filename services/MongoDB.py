from pymongo import MongoClient


class MongoDB:
    def __init__(self, connectionString: str) -> None:
        self.connection_string = connectionString

    def get_collection(self, collection_name):
        client = MongoClient(self.connection_string)
        return client['clickup_tasks'][collection_name]

    def insert_tasks(self, objects):
        task_collection = self.get_collection("tasks")
        task_collection.insert_many(objects)

    def delete_all_tasks(self):
        task_collection = self.get_collection("tasks")
        task_collection.delete_many({})

    def get_all_tasks(self):
        task_collection = self.get_collection("tasks")
        return task_collection.find()
