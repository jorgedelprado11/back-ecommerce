from db.models.product import Product
from db.schemas.product import product_schema, products_schema
from db.client import db_client
import json
import os
import requests


def data_products():
    path_name = "C:\\Users\\Jorge\\Desktop\\Back-Ecommerce\\data_products.json"

    if os.path.isfile(path_name):
        print("File exists")
        with open(path_name, 'r') as archivo:
            datos = archivo.read()
            products = json.loads(datos)['products']
            return products
    else:
        print("El archivo no existe, se encontró un error tipo IOError")


def cargar_datos(product: Product):
    product = dict(product)
    del product['id']
    id = db_client.products.insert_one(product).inserted_id

    new_product = product_schema(db_client.products.find_one({'_id': id}))

    Product(**new_product)
    print(f'nuevo producto insertado')


def cargar_productos():
    contador = 0
    products = data_products()
    for product in products:
        contador += 1
        cargar_datos(product)
    #     print(product)
    # print(contador)


cargar_productos()
