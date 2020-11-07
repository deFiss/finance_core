import pymongo
from os import getenv


class DataBase:
    def __init__(self):
        self.client = pymongo.MongoClient(
            host=getenv('DB_HOST'),
            port=int(getenv('DB_PORT')),
            authSource=getenv('DB_BASE_NAME'),
            username=getenv('DB_USER_NAME'),
            password=getenv('DB_USER_PASS'),
            authMechanism='SCRAM-SHA-1'

        )

        self.root = self.client[getenv('DB_BASE_NAME')]

    @staticmethod
    def cursor_to_list(cursor):
        result = []
        for item in cursor:
            if '_id' in item:
                item['_id'] = str(item['_id'])

            result.append(item)

        return result
