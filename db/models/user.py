from pydantic import BaseModel


class User(BaseModel):
    username: str
    nombre: str
    apellido: str
    # email: str
    # direccion: str | None = None
    disabled: bool
    # admin: bool


class UserPrivate(User):
    password: str
