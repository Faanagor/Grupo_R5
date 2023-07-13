from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union, Optional, List
from datetime import date


app = FastAPI()


@app.get('/')
async def root():
    return {'message': 'Hola FASTAPI'}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
# class Biblioteca(BaseModel):
#     id: int
#     titulo: str
#     subtítulo: str
#     autor: str
#     categoría: str
#     fecha_publicacion: date
#     editor: str
#     descripcion: str
#     imagen: str[Optional]
