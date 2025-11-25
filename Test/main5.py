#POST endpoint with Pydantic
from fastapi import FastAPI
from pydantic import BaseModel

class Product(BaseModel):
    name: str
    price: float

app = FastAPI()

@app.post("/products")
def add_product(product: Product):
    return {"received": product}
