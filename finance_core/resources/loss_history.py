from .base_resource import *
from datetime import datetime
import pytz


class LossHistoryList(BaseResource):
    def get(self):
        return {'loss_history': self.db.cursor_to_list(self.db.root['loss_history'].find())}

    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('deposit_id', type=str, required=True, dest=False)
        parser.add_argument('type_id', type=str, required=True, dest=False)
        parser.add_argument('quantity', type=int, required=True, dest=False)
        parser.add_argument('comment', type=str, required=False, dest=False)

        args = dict(parser.parse_args(strict=True))

        # check deposit_id
        try:
            if not self.db.root['deposits'].find_one({'_id': ObjectId(args['deposit_id'])}):
                raise Exception
            else:
                args['deposit_id'] = ObjectId(args['deposit_id'])
        except:
            abort(400, message='deposit_doesnt_exist')

        # check type_id
        try:
            if not self.db.root['types_of_losses'].find_one({'_id': ObjectId(args['type_id'])}):
                raise Exception
            else:
                args['type_id'] = ObjectId(args['type_id'])
        except:
            abort(400, message='types_of_losses_doesnt_exist')

        # add time
        args['time'] = datetime.now(tz=pytz.timezone('Europe/Moscow'))

        # insert
        self.db.root['loss_history'].insert(args)

        return {'message': 'ok'}
