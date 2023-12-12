from db.models.user import UserPrivate, User


def user_private_schema(user) -> dict:

    return {
        'username': user['username'],
        'nombre': user['nombre'],
        'apellido': user['apellido'],
        'disabled': user['disabled'],
        'password': user['password']
    }
# return {'id': user['_id'],
#         'username': user['username'],
#         'nombre': user['nombre'],
#         'apellido': user['apellido'],
#         'email': user['email'],
#         'direccion': user['direccion'],
#         'disabled': user['disabled'],
#         'admin': user['admin'],
#         'password': user['password']}


def user_schema(user) -> dict:

    return {
        'username': user['username'],
        'nombre': user['nombre'],
        'apellido': user['apellido'],
        'disabled': user['disabled']
    }
    # return {'id': user['_id'],
    #         'username': user['username'],
    #         'nombre': user['nombre'],
    #         'apellido': user['apellido'],
    #         'email': user['email'],
    #         'direccion': user['direccion'],
    #         'disabled': user['disabled'],
    #         'admin': user['admin']}


def users_schema(users) -> list:
    return [user_schema(user) for user in users]
