from flask import Flask

app = Flask(__name__)

stores = [
    {
        "name": "My Store",
        "items": [{"name": "Chair", "price": 15.99}, {"name": "Table", "price": 25.99}]
    },
    {
        "name": "My Store 2",
        "items": [{"name": "Milk", "price": 5.99}, {"name": "Eggs", "price": 2.99}]
    }
]

@app.get("/") # http://example.com/
def get_homepage():
    """returns all items within store array"""
    return "<h1>Hello World</h1>"

@app.get("/store") # http://yourdomain.com/store
def get_stores():
    """returns all items within store array"""
    return {"stores": stores}

@app.get("/store/item/{ids:int}") # http://example.com/store/item/id
def get_items(ids:int):
    """returns all items within store array"""
    return stores[ids]
