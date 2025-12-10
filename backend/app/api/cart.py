from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class CartItem(BaseModel):
    product_id: int
    quantity: int

class Cart(BaseModel):
    items: List[CartItem]

@app.post('/cart/')
def add_item_to_cart(cart_item: CartItem):
    return {'message': 'Item added to cart'}