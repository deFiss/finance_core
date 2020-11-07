from flask_restful import Resource, reqparse, abort
from data_base import DataBase
from flask import request, abort
import auth
from bson.objectid import ObjectId


class BaseResource(Resource):
    def __init__(self):
        self.db = DataBase()

    def dispatch_request(self, *args, **kwargs):

        # check JWT token
        try:
            token = request.headers['Authorization'].split('Bearer ')[1]
            auth.check_token_valid(self.db, token)
        except:
            abort(403)

        return super().dispatch_request(*args, **kwargs)