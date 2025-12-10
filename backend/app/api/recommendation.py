from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Recommendation(BaseModel):
    product_id: int
    recommended_products: List[int]

@app.get('/recommendations/')
def get_recommendations(product_id: int):
    return {'recommended_products': [1, 2, 3]}