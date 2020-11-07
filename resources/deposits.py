from .base_resource import *


class Deposits(BaseResource):
    def get(self, deposit_id):
        result = self.db.root['deposits'].find_one({'_id': ObjectId(deposit_id)})

        return {'deposit': self.db.cursor_to_list([result])[0]}

    def put(self, deposit_id):
        parser = reqparse.RequestParser()

        parser.add_argument('balance', type=int, help='New deposit balance', required=False, dest=False)
        parser.add_argument('name', type=str, help='New deposit name', required=False, dest=False)
        parser.add_argument('emoji', type=str, help='New deposit emoji', required=False, dest=False)

        args = dict(parser.parse_args(strict=True))

        # remove None args
        filtred_args = {}
        for k, v in args.items():
            if v:
                filtred_args[k] = v

        self.db.root['deposits'].update({'_id':  ObjectId(deposit_id)}, {"$set": filtred_args}, upsert=False)

        return {'message': 'ok'}


class DepositsList(BaseResource):
    def get(self):
        return {'deposits': self.db.cursor_to_list(self.db.root['deposits'].find())}