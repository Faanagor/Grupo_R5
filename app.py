from fastapi import FastAPI
from routers.libro import libro


app = FastAPI()
app.include_router(libro)
