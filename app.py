from fastapi import FastAPI
from routes.libro import libro


app = FastAPI()
app.include_router(libro)
