from flask_restful import Resource, reqparse, abort
from finance_core.data_base import DataBase
from flask import request, abort
from finance_core import auth
from bson.objectid import ObjectId


class BaseResource(Resource):
    def __init__(self, fields, db_collection_name):
        self.db = DataBase()

        self.fields = fields
        self.db_collection_name = db_collection_name

        self.collection = self.db.root[self.db_collection_name]

    def get(self, object_id=None):
        if not object_id:
            return {'data': self.db.cursor_to_list(self.collection.find())}

        result = self.collection.find_one({'_id': ObjectId(object_id)})

        if not result:
            abort(404)

        return {'data': self.db.cursor_to_list([result])[0]}

    def delete(self, object_id):
        self.collection.delete_one({'_id': ObjectId(object_id)})
        return {'message': 'ok'}

    def put(self, object_id):
        parser = reqparse.RequestParser()

        for field in self.fields:
            parser.add_argument(**field, required=False, dest=False)

        args = dict(parser.parse_args(strict=True))

        # remove None args
        filtred_args = {}
        for k, v in args.items():
            if v:
                filtred_args[k] = v

        self.collection.update({'_id': ObjectId(object_id)}, {"$set": filtred_args}, upsert=False)
        return {'message': 'ok'}

    def post(self):
        parser = reqparse.RequestParser()

        for field in self.fields:
            parser.add_argument(**field, required=True, dest=False)

        args = dict(parser.parse_args(strict=True))

        self.collection.insert(args)

        return {'message': 'ok'}

    def dispatch_request(self, *args, **kwargs):

        # check JWT token
        try:
            token = request.headers['Authorization'].split('Bearer ')[1]
            auth.check_token_valid(self.db, token)
        except:
            abort(403)

        return super().dispatch_request(*args, **kwargs)

    @staticmethod
    def _convert_time(time):
        return time.strftime('%Y-%m-%dT%H:%M:%SZ')

    def __repr__(self):
        return self.db_collection_name
