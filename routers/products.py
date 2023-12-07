from fastapi import APIRouter, status, HTTPException
from fastapi.responses import JSONResponse
from db.models.product import Product
from db.schemas.product import product_schema, products_schema
from db.client import db_client
from bson import ObjectId
from handlers.search_product import search_product


router = APIRouter(prefix="/product",
                   tags=["product"],
                   responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})


# @router.get('/')
# # controlador para traer un producto por categoria (query)
# async def products(categoria: str):
#     return search_products('categoria', categoria)


@router.get('/', response_model=list[Product], status_code=status.HTTP_200_OK)
# controlador para traer todos los productos
async def products():
    try:
        return products_schema(db_client.products.find())
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Productos no encontrados")


@router.get('/{id}', status_code=status.HTTP_200_OK)
# controlador para traer un producto por id
async def product(id: str):
    try:
        return search_product('_id', ObjectId(id))
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Producto no encontrado")


@router.post('/', response_model=Product, status_code=status.HTTP_201_CREATED)
# controlador para crear un nuevo producto
async def product(product: Product):
    try:
        product = dict(product)
        del product['id']

        id = db_client.products.insert_one(product).inserted_id

        new_product = product_schema(db_client.products.find_one({'_id': id}))

        return Product(**new_product)
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="No se pudo crear el Producto")


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
# controlador para eliminar producto 
async def product(id: str):
    try:
        found = db_client.products.find_one_and_delete({'_id': ObjectId(id)})
        if not found:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Producto no encontrado")
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Producto no encontrado")


@router.put('/', response_model=Product, status_code=status.HTTP_200_OK)
# controlador para actualizar producto
async def product(product: Product):
    product_update = dict(product)
    del product_update['id']
    try:
        db_client.products.find_one_and_replace(
            {'_id': ObjectId(product.id)}, product_update)

    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Producto no encontrado')
    return search_product('_id', ObjectId(product.id))
