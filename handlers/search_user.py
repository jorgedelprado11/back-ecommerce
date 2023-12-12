from db.client import db_client
from db.schemas.user import user_private_schema, user_schema, users_schema
from db.models.user import UserPrivate, User


def search_user_private(username: str):
    return user_private_schema(db_client.users.find_one({'username': username}))


def search_user(field: str, key: str):
    return User(**user_schema(db_client.users.find_one({field: key})))
