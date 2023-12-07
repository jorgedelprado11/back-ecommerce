from pymongo import MongoClient


# Base de datos local mongoDB
db_client = MongoClient().local


# Base de datos remota MongoDB Atlas (https://mongodb.com)
# db_client = MongoClient(
#     "mongodb+srv://e-commerce:<password>@cluster0.srk4yun.mongodb.net/?retryWrites=true&w=majority").test

# Despliegue API en la nube:
# Deta - https://www.deta.sh/
# Intrucciones - https://fastapi.tiangolo.com/deployment/deta/
