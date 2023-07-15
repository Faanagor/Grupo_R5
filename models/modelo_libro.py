from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date

from sqlalchemy import Table, Column, Integer, String
from config.db import meta, engine

libros = Table('Libros', meta,
               Column('id', Integer, primary_key=True),
               Column('titulo', String(255)),
               Column('subtítulo', String(255)),
               Column('autor', String(255)),
               Column('categoría', String(255)),
               Column('fecha_publicacion', String(255)),
               Column('editor', String(255)),
               Column('descripcion', String(255)),
               Column('imagen', String(255)),
               )

meta.create_all(engine)


"""
class MiModelo(Base):
    __tablename__ = 'nombre_tabla'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50))
    edad = Column(Integer)
    correo = Column(String(100))

"""


# class Libro(BaseModel):
#     id: int
#     titulo: str
#     subtítulo: str
#     autor: str
#     categoría: str
#     fecha_publicacion: date
#     editor: Union[str, None] = None
#     descripcion: str
#     imagen: str[Optional]


app = FastAPI()
