from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Review(BaseModel):
    id: int
    product_id: int
    user_id: int
    review: str
    rating: int

@app.post('/reviews/')
def create_review(review: Review):
    return {'message': 'Review created successfully'}