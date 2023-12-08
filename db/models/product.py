from pydantic import BaseModel
from typing import Optional
# Product Model


class Product(BaseModel):
    id: Optional[str]
    nombre: str
    categoria: str
    precio: int | float
    stock: int
    imagenes: list
    caracteristicas: Optional[dict]
