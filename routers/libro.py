from fastapi import APIRouter
from config.db import conn
from models.modelo_libro import libros
# from pydantic import BaseModel
# from typing import Union, Optional, List
# from datetime import date


libro = APIRouter()


@libro.get('/libros')
def get_libros():
    return conn.execute(libros.select()).fetchall()


# @libro.get('/crear_libro')
# async def crear_libro(libro: Libro):
#     return {'message': 'INGRESAR LIBRO'}


# @libro.get('/show_libros')
# async def show_root():
#     return {'message': 'MOSTRAR LIBROS'}


# @libro.get('/update')
# async def update_root():
#     return {'message': 'ACTUALIZAR INFO DE LIBRO'}


# @libro.get("/items/{item_id}")
# async def read_item(item_id: int):
#     return {"item_id": item_id}
