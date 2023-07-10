from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union, Optional, List


app = FastAPI()


class Biblioteca(BaseModel):
    id: int
    titulo: str
    subtítulo: str
    autor: str
    categoría: str
    fecha_publicacion: str
    editor: str
    descripcion: str
    imagen: str[Optional]

