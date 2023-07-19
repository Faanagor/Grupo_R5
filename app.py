from fastapi import FastAPI
from routers.libros import libro


app = FastAPI()
app.include_router(libro)
