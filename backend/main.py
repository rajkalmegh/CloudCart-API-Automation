
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import uuid

app = FastAPI()

users_db = {}
products_db = {}
orders_db = {}

class User(BaseModel):
    username: str
    password: str

class Product(BaseModel):
    name: str
    price: float

class Order(BaseModel):
    product_id: str
    quantity: int

@app.post("/register")
def register(user: User):
    if user.username in users_db:
        raise HTTPException(status_code=400, detail="User already exists")
    users_db[user.username] = user.password
    return {"message": "User registered"}

@app.post("/login")
def login(user: User):
    if users_db.get(user.username) != user.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = str(uuid.uuid4())
    return {"token": token}

@app.post("/products")
def create_product(product: Product):
    product_id = str(uuid.uuid4())
    products_db[product_id] = product
    return {"id": product_id, "product": product}

@app.get("/products")
def get_products():
    return products_db

@app.get("/products/{product_id}")
def get_product(product_id: str):
    if product_id not in products_db:
        raise HTTPException(status_code=404)
    return products_db[product_id]

@app.post("/orders")
def create_order(order: Order):
    order_id = str(uuid.uuid4())
    orders_db[order_id] = order
    return {"order_id": order_id, "order": order}

@app.get("/orders/{order_id}")
def get_order(order_id: str):
    if order_id not in orders_db:
        raise HTTPException(status_code=404)
    return orders_db[order_id]
