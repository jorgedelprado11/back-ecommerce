from pydantic import BaseModel

# Product Model


class Product(BaseModel):
    id: str | None = None
    nombre: str
    categoria: str
    precio: int | float
    stock: int
    imagenes: list
    caracteristicas: dict | None = None
