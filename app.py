from flask import Flask, request

app = Flask(__name__)

stores = [
    {   "store_id": 1,
        "name": "bronx",
        "items": [{"name": "Chair", "price": 125.99}, {"name": "Table", "price": 225.99}]
    },
    {
        "store_id": 2,
        "name": "brooklyn",
        "items": [{"name": "Milk", "price": 55.99}, {"name": "Eggs", "price": 22.99}]
    },
    {
        "store_id": 3,
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
    """returns a store based on its name."""
    for item in stores:
        if item["name"] == name:
            return item, 200

@app.get("/store/<int:store_id>")
def get_store_by_id(store_id):
    """returns a store based on its id(index + 1)item."""
    result = {"store": None}
    for store in stores:
        if store["store_id"] == store_id:
            result["store"] = store
            return result, 200
    return result,404

@app.post("/store")
def create_store():
    """returns the most recently added item."""
    req_data = request.get_json()
    print(type(req_data))
    stores.append(req_data)
    return stores[-1], 201
