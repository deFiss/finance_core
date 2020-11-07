import jwt
import os
from bson.objectid import ObjectId


def check_token_valid(db, token):
    key = os.getenv('JWT_SECRET_KEY')

    decoded = jwt.decode(token, key, algorithms='HS256')
    user_id = decoded['id']

    if not db.root['users'].find_one({'_id': ObjectId(user_id)}):
        raise Exception

    # enc = jwt.encode({'id': '5f6f7a193439e03ba1755619'}, key, algorithm='HS256')

