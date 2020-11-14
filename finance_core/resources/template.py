from .base_resource import *


class Template(BaseResource):
    
    def __init__(self):
        db_collection_name = 'template'

        fields = [
            {'name': 'name', 'type': str},
            {'name': 'emoji', 'type': str},

            {'name': 'deposit', 'type': str},
            {'name': 'amount', 'type': int},
            {'name': 'type', 'type': str},
        ]

        super().__init__(fields, db_collection_name)
