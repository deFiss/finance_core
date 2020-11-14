from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from dotenv import load_dotenv
import os

from finance_core.resources import *


class Server:
    def __init__(self):
        self.resources = [
            Deposit,
            Template,

            TypeOfIncome,
            TypeOfLoss,

            IncomeHistory,
            LossHistory
        ]

        self.api_prefix = '/api/v1/'

        self.app = None
        self.api = None

    def config_app(self):
        self.app = Flask(__name__)
        self.api = Api(self.app)
        CORS(self.app)

        self._add_resources()

        return self.app

    def _add_resources(self):

        for resource in self.resources:
            resource_name = str(resource())

            model_url_path = f'{self.api_prefix}{resource_name}/'
            object_url_path = model_url_path + '<string:object_id>/'

            self.api.add_resource(resource, object_url_path, model_url_path)


if __name__ == '__main__':
    load_dotenv()
    server = Server()
    app = server.config_app()

    app.run(
        host=os.getenv('SERVER_HOST'),
        port=int(os.getenv('SERVER_PORT')),
        debug=True
    )
