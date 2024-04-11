import copy
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
    return '<html><head><meta name="title" content="Build REST APIs with Flask and Python (The Complete Course)"></head><body><h1>The REST store app</body</html>', 200

@app.get("/store") #http://example.com/store
def get_all_stores():
    """returns container stores"""
    return {"stores": stores}, 200

@app.get("/store/<string:name>") #http://example.com/store/brooklyn
def get_store_by_name(name):
    """returns a store based on its name."""
    result = {"store": None}
    for item in stores:
        if item["name"] == name:
            result = item
            return result, 200
    return result,404

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
def add_new_store():
    """returns the most recently added item."""
    req_data = request.get_json()
    new_store = {
        "store_id": len(stores) + 1,
        "name": req_data["name"],
        "items": req_data["items"]
    }
    print(new_store)
    stores.append(new_store)
    return stores[-1], 201

@app.post("/store/<string:store_name>/item")
def add_new_item(store_name):
    requested_data = request.get_json()
    item_name, item_price = requested_data["name"], requested_data["price"]
    for store in stores:
        if store["name"] == store_name:
            store["items"].append({"name": item_name, "price": item_price})
            return store, 201
    return {"message": "Store was not found or Invalid store."}, 404

@app.get("/store/<string:store_name>/item")
def get_store_items(store_name):
    for store in stores:
        if store["name"] == store_name:
            return {"items": store["items"]}, 200
    return {"message": "Store not found!"}, 404

@app.post("/store/<string:store_name>/<string:item_name>/<float:new_price>")
def update_item_price(store_name, item_name, new_price):
    store = [store for store in stores if store["name"] == store_name]
    if not store:
        return {"message": "Store not found!"}, 404
    old_store = copy.deepcopy(store[0])
    for item in store[0]["items"]:
        if item["name"] == item_name:
            item["price"] = float(new_price)
            return {"before": old_store, "after": store},201
    return {"message": "Item not found!"}, 404

