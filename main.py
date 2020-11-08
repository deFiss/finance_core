from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from dotenv import load_dotenv
import os

from finance_core.resources import *

app = Flask(__name__)
api = Api(app)
CORS(app)

API_PREFIX = '/api/v1/'

api.add_resource(Deposits, API_PREFIX + 'deposits/<string:deposit_id>/')
api.add_resource(DepositsList, API_PREFIX + 'deposits/')

api.add_resource(TypesOfIncome, API_PREFIX + 'type_of_income/<string:type_of_income_id>/')
api.add_resource(TypesOfIncomeList, API_PREFIX + 'type_of_income/')

api.add_resource(TypesOfLosses, API_PREFIX + 'type_of_loss/<string:types_of_losses_id>/')
api.add_resource(TypesOfLossesList, API_PREFIX + 'type_of_loss/')

api.add_resource(IncomeHistoryList, API_PREFIX + 'income_history/')

api.add_resource(LossHistoryList, API_PREFIX + 'loss_history/')


if __name__ == '__main__':
    load_dotenv()
    app.run(host=os.getenv('SERVER_HOST'), port=int(os.getenv('SERVER_PORT')), debug=True)