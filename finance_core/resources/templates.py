from .base_resource import *


class Templates(BaseResource):
    def get(self, template_id):
        result = self.db.root['templates'].find_one({'_id': ObjectId(template_id)})

        return {'template': self.db.cursor_to_list([result])[0]}

    def put(self, template_id):
        parser = reqparse.RequestParser()

        parser.add_argument('name', type=str, required=False, dest=False)
        parser.add_argument('emoji', type=str, required=False, dest=False)

        parser.add_argument('deposit', type=str, required=False, dest=False)
        parser.add_argument('amount', type=int, required=False, dest=False)
        parser.add_argument('type', type=str, required=False, dest=False)

        args = dict(parser.parse_args(strict=True))

        # remove None args
        filtred_args = {}
        for k, v in args.items():
            if v:
                filtred_args[k] = v

        self.db.root['templates'].update({'_id':  ObjectId(template_id)}, {"$set": filtred_args}, upsert=False)

        return {'message': 'ok'}

    def delete(self, template_id):
        self.db.root['templates'].delete_one({'_id':  ObjectId(template_id)})

        return {'message': 'ok'}


class TemplatesList(BaseResource):
    def get(self):
        return {'templates': self.db.cursor_to_list(self.db.root['templates'].find())}

    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('name', type=str, required=True, dest=False)
        parser.add_argument('emoji', type=str, required=True, dest=False)

        parser.add_argument('deposit', type=str, required=True, dest=False)
        parser.add_argument('amount', type=int, required=True, dest=False)
        parser.add_argument('type', type=str, required=True, dest=False)

        args = dict(parser.parse_args(strict=True))

        self.db.root['templates'].insert(args)

        return {'message': 'ok'}
