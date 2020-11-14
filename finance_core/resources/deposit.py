from .base_resource import *


class Deposit(BaseResource):
    def __init__(self):
        db_collection_name = 'deposit'

        fields = [
            {'name': 'balance', 'type': int},
            {'name': 'name', 'type': str},
            {'name': 'emoji', 'type': str},
            {'name': 'symbol', 'type': str},

        ]

        super().__init__(fields, db_collection_name)
