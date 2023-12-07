from db.models.product import Product
from db.schemas.product import product_schema, products_schema
from db.client import db_client


def search_product(field: str, key):
    # funcion generica para buscar productos por field, key
    try:
        product = product_schema(db_client.products.find_one({field: key}))
        return Product(**product)
    except:
        return {"error": "No se ha encontrado el producto que buscas"}


# def search_products(field: str, key):
#     # funcion generica para buscar productos por field, key
#     try:
#         all_products = []
#         # creo el index para buscar por texto
#         db_client.products.create_index({field: "text"})
#         # busco por texto en la DB, con con case insentive
#         products_found = products_schema(
#             db_client.products.find({"$text": {"$search": key, "$caseSensitive": False}}))

#         for product in products_found:
#             all_products.append(Product(**product))
#         return all_products
#     except:
#         return {"error": "No se han encontrado los productos que buscas"}
