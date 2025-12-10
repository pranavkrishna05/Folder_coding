from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Order(BaseModel):
    id: int
    user_id: int
    order_date: str
    total: float

@app.post('/orders/')
def create_order(order: Order):
    return {'message': 'Order created successfully'}