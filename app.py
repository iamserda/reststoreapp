from flask import Flask, request
import json

app = Flask("__name__")

inwood_library = {
    "books": [{"id": 1, "title": "1984", "author": "George Orwell", "publisher": "Penguin"}],
    "movies": [],
    "events": [],
    }

@app.route("/api/books/")
def get_books():
    return { "books": inwood_library["books"]}

@app.route("/api/book/<int:id>")
def get_book_by_id(id):
    for book in inwood_library.get("books"):
        if book["id"] == id:
            return {"book": book}
        else:
            return {"message": "404: Not Found!"}, 404

@app.post("/api/book")
def add_new_book():
    book_info = request.get_json()
    new_book = {"id": len(inwood_library["books"]) + 1}
    for k,v in book_info.items():
        new_book[k] = v    
    inwood_library["books"].append(new_book)
    return inwood_library["books"][-1]
    


@app.get("/api/movies/")
def get_movies():
    return { "movies": inwood_library["movies"]}