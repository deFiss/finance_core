from .base_resource import *


class TypesOfIncome(BaseResource):
    def get(self, types_of_income_id):
        result = self.db.root['types_of_income'].find_one({'_id': ObjectId(types_of_income_id)})

        return {'type_of_income': self.db.cursor_to_list([result])[0]}

    def put(self, type_of_income_id):
        parser = reqparse.RequestParser()

        parser.add_argument('name', type=str, help='New types_of_income name', required=False, dest=False)
        parser.add_argument('emoji', type=str, help='New types_of_income emoji', required=False, dest=False)

        args = dict(parser.parse_args(strict=True))

        # remove None args
        filtred_args = {}
        for k, v in args.items():
            if v:
                filtred_args[k] = v

        self.db.root['types_of_income'].update(
            {'_id':  ObjectId(type_of_income_id)},
            {"$set": filtred_args},
            upsert=False
        )

        return {'message': 'ok'}

    def delete(self, type_of_income_id):
        self.db.root['types_of_income'].delete_one({'_id': ObjectId(type_of_income_id)})
        return {'message': 'ok'}


class TypesOfIncomeList(BaseResource):
    def get(self):
        return {'types_of_income': self.db.cursor_to_list(self.db.root['types_of_income'].find())}

    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('name', type=str, help='types_of_income name', required=True, dest=False)
        parser.add_argument('emoji', type=str, help='types_of_income emoji', required=True, dest=False)

        args = dict(parser.parse_args(strict=True))

        self.db.root['types_of_income'].insert(args)

        return {'message': 'ok'}
