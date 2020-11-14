from .base_resource import *


class TypeOfLoss(BaseResource):
    def __init__(self):
        db_collection_name = 'type_of_loss'

        fields = [
            {'name': 'name', 'type': str},
            {'name': 'emoji', 'type': str},

        ]

        super().__init__(fields, db_collection_name)
