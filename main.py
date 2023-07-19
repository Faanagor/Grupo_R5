# from fastapi import FastAPI
# from pydantic import BaseModel
# from typing import Union, Optional, List
# from datetime import date


# app = FastAPI()


# @app.get('/')
# def root():
#     return {'message': 'Hola FASTAPI'}


# @app.get("/items/{item_id}")
# def read_item(item_id: int):
#     return {"item_id": item_id}
# class Biblioteca(BaseModel):
#     id: int
#     titulo: str
#     subtitulo: str
#     autor: str
#     categoria: str
#     fechapublicacion: date
#     editor: str
#     descripcion: str
#     imagen: str[Optional]
