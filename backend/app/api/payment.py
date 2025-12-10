from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Payment(BaseModel):
    id: int
    order_id: int
    payment_method: str
    payment_date: str

@app.post('/payments/')
def process_payment(payment: Payment):
    return {'message': 'Payment processed successfully'}