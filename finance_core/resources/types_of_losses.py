from .base_resource import *


class TypesOfLosses(BaseResource):
    def get(self, types_of_losses_id):
        result = self.db.root['types_of_losses'].find_one({'_id': ObjectId(types_of_losses_id)})

        return {'types_of_loss': self.db.cursor_to_list([result])[0]}

    def put(self, types_of_losses_id):
        parser = reqparse.RequestParser()

        parser.add_argument('name', type=str, help='New types_of_losses name', required=False, dest=False)
        parser.add_argument('emoji', type=str, help='New types_of_losses emoji', required=False, dest=False)

        args = dict(parser.parse_args(strict=True))

        # remove None args
        filtred_args = {}
        for k, v in args.items():
            if v:
                filtred_args[k] = v

        self.db.root['types_of_losses'].update(
            {'_id':  ObjectId(types_of_losses_id)},
            {"$set": filtred_args},
            upsert=False
        )

        return {'message': 'ok'}

    def delete(self, types_of_losses_id):
        self.db.root['types_of_losses'].delete_one({'_id': ObjectId(types_of_losses_id)})
        return {'message': 'ok'}


class TypesOfLossesList(BaseResource):
    def get(self):
        return {'types_of_losses': self.db.cursor_to_list(self.db.root['types_of_losses'].find())}

    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('name', type=str, help='types_of_losses name', required=True, dest=False)
        parser.add_argument('emoji', type=str, help='types_of_losses emoji', required=True, dest=False)

        args = dict(parser.parse_args(strict=True))

        self.db.root['types_of_losses'].insert(args)

        return {'message': 'ok'}
