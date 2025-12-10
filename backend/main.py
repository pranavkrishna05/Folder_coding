from fastapi import FastAPI, Depends
from backend.routes import user_router, product_router, cart_router, order_router