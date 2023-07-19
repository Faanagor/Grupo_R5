from typing import Optional
from pydantic import BaseModel
from datetime import date


class LibroSchema(BaseModel):
    id: Optional[int]
    titulo: str
    subtitulo: str
    autor: str
    categoria: str
    fechapublicacion: date
    editor: Optional[str]
    descripcion: str
    imagen: Optional[str]


class UserCount(BaseModel):
    total: int
