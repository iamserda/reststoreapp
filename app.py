from flask import Flask, request

app = Flask(__name__)

stores = [
    {
        "name": "bronx",
        "items": [{"name": "Chair", "price": 125.99}, {"name": "Table", "price": 225.99}]
    },
    {
        "name": "brooklyn",
        "items": [{"name": "Milk", "price": 55.99}, {"name": "Eggs", "price": 22.99}]
    },
    {
    "name": "manhattan",
    "items": [{"name": "Milk", "price": 55.99}, {"name": "Eggs", "price": 22.99}]
    }
]

@app.get("/") # http://example.com/
def get_homepage():
    """returns all items within store array"""
    return "<h1>Hello World</h1>"

@app.get("/store")
def get_all_stores():
    """returns container stores"""
    return {"stores": stores}

@app.get("/store/<string:name>")
def get_store_by_name(name):
    for item in stores:
        if item["name"] == name:
            return item, 200

@app.post("/store")
def create_store():
    """returns the most recently added item."""
    req_data = request.get_json()
    print(type(req_data))
    stores.append(req_data)
    return stores[-1], 201

