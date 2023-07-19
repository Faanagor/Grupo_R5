from typing import List
from fastapi import APIRouter  # , Response, status
# from starlette.status import HTTP_204_NO_CONTENT
from config.db import conn
from models.modelo_libro import libros
from schemas.schema_libro import LibroSchema
# from pydantic import BaseModel
# from typing import Union, Optional, List
# from datetime import date


libro = APIRouter()


# @libro.get('/', response_model=List[LibroSchema], tags='libros')
# def root():
#     return {'message': 'Biblioteca Grupo R5'}


@libro.get('/libros', response_model=List[LibroSchema], tags='libros')
def get_libros():
    rows = conn.execute(libros.select()).fetchall()
    # Iterar sobre las filas y mostrar los datos
    for row in rows:
        print(row)
    return rows


@libro.post('/crear_libro', response_model=LibroSchema,
            tags='libros', description="Crea nuevo libro")
def crear_libro(libro: LibroSchema):
    print(libro)
    nuevo_libro = {
                   'id': libro.id,
                   'titulo': libro.titulo,
                   'subtitulo': libro.subtitulo,
                   'autor': libro.autor,
                   'categoria': libro.categoria,
                   'fechapublicacion': libro.fechapublicacion,
                   'editor': libro.editor,
                   'descripcion': libro.descripcion,
                   'imagen': libro.imagen
                   }
    result = conn.execute(libros.insert().values(nuevo_libro))
    print(result)
    # print('Funcion Crear libro ha corrido')
    print("Se ha agregado un nuevo libro a la BD")
    return conn.execute(libros.select().where(libros.c.id == result.lastrowid)).first()


'''
@libro.get('/libros/{id}', response_model=LibroSchema, tags='libros')
def obtener_libro(id: str):
    return conn.execute(libros.select().where(libros.c.id == id)).first()


@libro.delete('/libros/{id}', status_code=status.HTTP_204_NO_CONTENT,
              tags='libros')
def eliminar_libro(id: str):
    conn.execute(libros.delete().where(libros.c.id == id)).first()
    return Response(status_code=HTTP_204_NO_CONTENT)


@libro.put('/libros/{id}', response_model=LibroSchema, tags='libros')
def actualizar_libro(id: str, libro: LibroSchema):
    nuevo_libro = {'titulo': libro.titulo,
                   'subtitulo': libro.subtitulo,
                   'autor': libro.autor,
                   'categoria': libro.categoria,
                   'fechapublicacion': libro.fechapublicacion,
                   'editor': libro.editor,
                   'descripcion': libro.descripcion,
                   'imagen': libro.imagen
                   }
    conn.execute(libros.update().values(nuevo_libro).where(libros.c.id == id))
    return conn.execute(libros.select().where(libros.c.id == id)).first()
'''
