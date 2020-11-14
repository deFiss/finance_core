from .base_resource import *
from datetime import datetime
import pytz


class LossHistory(BaseResource):
    def __init__(self):
        db_collection_name = 'loss_history'

        fields = [
            {'name': 'deposit_id', 'type': str},
            {'name': 'type_id', 'type': str},
            {'name': 'quantity', 'type': int},
            {'name': 'comment', 'type': str},
        ]

        super().__init__(fields, db_collection_name)

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
