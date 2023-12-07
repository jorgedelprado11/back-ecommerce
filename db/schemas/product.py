from db.models.product import Product


# devuelve cada producto individualmente
def product_schema(product) -> Product:

    return {'id': str(product['_id']),
            'nombre': product['nombre'],
            'categoria': product['categoria'],
            'precio': product['precio'],
            'stock': product['stock'],
            'imagenes': product['imagenes'],
            'caracteristicas': product['caracteristicas']}

# devuelve toda la lista de productos


def products_schema(products) -> list:

    return [product_schema(product) for product in products]
