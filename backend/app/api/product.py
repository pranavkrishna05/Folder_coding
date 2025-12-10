from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Product(BaseModel):
    id: int
    name: str
    price: float
    category: str

class ProductCategory(BaseModel):
    id: int
    name: str

@app.get('/products/')
def read_products():
    return [{'id': 1, 'name': 'Product 1', 'price': 10.99, 'category': 'Category 1'}, {'id': 2, 'name': 'Product 2', 'price': 9.99, 'category': 'Category 2'}]