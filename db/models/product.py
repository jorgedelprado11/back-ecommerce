from pydantic import BaseModel
from typing import Optional
# Product Model


class Product(BaseModel):
    id: str | None = None
    nombre: str
    categoria: str
    precio: int | float
    stock: int
    imagenes: list
    caracteristicas: dict | None = None
