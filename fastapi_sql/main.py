from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    description: str
    price: int
    on_offer: bool

    class Config:
        orm_mode = True



# @app.get("/")
# def index():
#     return {"message": "Hello world"}

# @app.get("/greet/{name}")
# def greet_name(name: str):
#     return {"greeting": f"Hello {name}"}

# @app.get("/greet")
# def greet_optional_name(name: Optional[str]= "user"): # user as default value
#     return {"message": f"Hello {name}"}

@app.put("/item/{item_id}")
def update_item(item_id: int, item: Item):
    return {
        "name": item.name,
        "description": item.description,
        "price": item.price,
        "on_offer": item.on_offer
    }

    
