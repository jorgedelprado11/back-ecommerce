from fastapi import APIRouter, status, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from db.client import db_client
from db.schemas.user import user_private_schema, user_schema
from handlers.search_user import search_user, search_user_private
from db.models.user import UserPrivate, User
from jose import jwt, JWTError
from datetime import datetime, timedelta
from db.models.token import Token, TokenData

# primerio instancio que tipo de algoritmo voy a usar
ALGORITHM = 'HS256'
# cuanto tiempo va a durar el access token en minutos
ACCESS_TOKEN_DURATION = 1
# e instancio tmb la semilla o secret
SECRET = '123hsjdfhqn2r34bvxiapskdanqkj'

router = APIRouter(prefix="/user",
                   tags=["user"],
                   responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})

oauth2 = OAuth2PasswordBearer(tokenUrl='login')

crypt = CryptContext(schemes=["bcrypt"], deprecated="auto")


#############################################
# verificaciones para el login:


def verify_password(plain_password, hashed_password):
    return crypt.verify(plain_password, hashed_password)


def get_password_hash(password):
    return crypt.hash(password)


def get_user(username: str):
    return UserPrivate(**db_client.users.find_one({'username': username}))


def autenticate_user(username: str, password: str):
    user = get_user(username)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)

    to_encode.update({'exp': expire})
    encode_jwt = jwt.encode(to_encode, SECRET, algorithm=ALGORITHM)
    return encode_jwt


async def get_current_user(token: str = Depends(oauth2)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="No se pudieron validar las credenciales",
                                          headers={"WWW-Authenticate": "Bearer"},)

    try:
        payload = jwt.decode(token, SECRET, algorithms=[ALGORITHM])
        username: str = payload.get('sub')
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user(username=token_data.username)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail='Usuario inactivo')
    return current_user
#############################################


@router.post('/register', status_code=status.HTTP_201_CREATED)
async def register(user: UserPrivate):
    try:
        found = db_client.users.find_one({'username': user.username})
        if not found:
            user.password = get_password_hash(user.password)
            user = dict(user)

            db_client.users.insert_one(user)

            return {'message': 'Usuario creado con éxito!'}
        raise
    except:
        if not found:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="No se pudo crear el usuario")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'El ususario {user.username} ya esta registrado')


@router.post('/login')
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user = autenticate_user(form.username, form.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='Usuario o Contraseña Incorrecta', headers={"WWW-Authenticate": "Bearer"})
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_DURATION)
    access_token = create_access_token(
        data={'sub': user.username}, expires_delta=access_token_expires)

    return {'access_token': access_token, 'token_type': 'bearer'}


@router.get('/me')
async def me(user: User = Depends(get_current_active_user)):

    return user
