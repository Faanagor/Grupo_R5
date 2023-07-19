from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta, engine
# from sqlalchemy import Column, Integer, String, ForeignKey, Text
# from pydantic import BaseModel
# from datetime import date
# from typing import Optional  # Union, List, Dict


libros = Table('libros', meta,
               Column('id', Integer, primary_key=True),
               Column('titulo', String(255)),
               Column('subtitulo', String(255)),
               Column('autor', String(255)),
               Column('categoria', String(255)),
               Column('fechapublicacion', String(255)),
               Column('editor', String(255)),
               Column('descripcion', String(255)),
               Column('imagen', String(255)),
               )

meta.create_all(engine)
# class Libro(BaseModel):
#     __tablename__ = "libros"
#     id = Column(Integer, primary_key=True, index=True)
#     titulo = Column(String, index=True)
#     subtitulo = Column(String, index=True, nullable=True)
#     fecha_publicacion = Column(String, nullable=True)
#     editor_id = Column(Integer, ForeignKey("editores.id"), nullable=True)
#     descripcion = Column(Text, nullable=True)
#     imagen = Column(String, nullable=True)
    
    
#     titulo: str
#     subtitulo: str
#     autor: str
#     categoria: str
#     fechapublicacion: date
#     editor: Optional[str]
#     descripcion: str
#     imagen: Optional[str]
