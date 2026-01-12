"""" Mon API """

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class MaClasse(BaseModel):
    """ Mon modèle de données """
    text: str

@app.get("/")
def root():
    """ Mon endpoint principal """
    return {"message": "Hello World"}