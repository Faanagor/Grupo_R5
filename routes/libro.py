from fastapi import APIRouter
# from pydantic import BaseModel
# from typing import Union, Optional, List
# from datetime import date


libro = APIRouter()


@libro.get('/')
async def root():
    return {'message': 'BIBLIOTECA'}


@libro.get('/create')
async def create_root():
    return {'message': 'INGRESAR LIBRO'}


@libro.get('/libros')
async def show_root():
    return {'message': 'MOSTRAR LIBROS'}


@libro.get('/update')
async def update_root():
    return {'message': 'ACTUALIZAR INFO DE LIBRO'}


@libro.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}