import jwt
import os
from bson.objectid import ObjectId
from dotenv import load_dotenv


def check_token_valid(db, token):
    key = os.getenv('JWT_SECRET_KEY')

    decoded = jwt.decode(token, key, algorithms='HS256')
    user_id = decoded['id']

    if not db.root['users'].find_one({'_id': ObjectId(user_id)}):
        raise Exception

    enc = jwt.encode({'id': '5f6f7a193439e03ba1755619'}, key, algorithm='HS256')


def encode(user_id):
    key = os.getenv('JWT_SECRET_KEY')
    enc = jwt.encode({'id': user_id}, key, algorithm='HS256')
    return enc


if __name__ == '__main__':
    load_dotenv()
    db_id = input('db_id: ')