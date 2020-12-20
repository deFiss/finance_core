from .base_resource import *
from datetime import datetime
import pytz


class IncomeHistory(BaseResource):
    def __init__(self):
        db_collection_name = 'income_history'

        fields = [
            {'name': 'deposit_id', 'type': str},
            {'name': 'type_id', 'type': str},
            {'name': 'quantity', 'type': int},
            {'name': 'comment', 'type': str},
        ]

        super().__init__(fields, db_collection_name)

    def get(self, object_id=None):
        if not object_id:

            data = self.db.cursor_to_list(self.collection.find())
            for d in data:
                d['time'] = self._convert_time(d['time'])

            return {'data': data}

        result = self.collection.find_one({'_id': ObjectId(object_id)})

        if not result:
            abort(404)

        data = self.db.cursor_to_list([result])[0]
        data['time'] = self._convert_time(data['time'])
        return {'data': data}

    def post(self):
        parser = reqparse.RequestParser()

        for field in self.fields:

            if field['name'] == 'comment':
                parser.add_argument(**field, required=False, dest=False)
                continue

            parser.add_argument(**field, required=True, dest=False)

        args = dict(parser.parse_args(strict=True))

        args['time'] = datetime.now(tz=pytz.timezone('Europe/Moscow'))

        self.collection.insert(args)

        return {'message': 'ok'}