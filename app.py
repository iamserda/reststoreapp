from flask import Flask, request
from database import events, books, movies
from flask_smorest import abort
from helpers import add_new_books

app = Flask("__name__")

@app.get("/")
def show_homepage():
    return """
<!DOCTYPE html>
<html>
    <head></head>
    <body>
        <header>
            <section>
                <div>
                    <h1>Welcome to the Home Library API</h1>
                </div>
            </section>
        </header>
        <main>
        </main>
        <footer>
            <p>Copyright &copy 2024, S Home Library Company, Inc.</p>
        </footer>
    </body>
</html>
"""

@app.route("/api/books/", methods=["GET", "POST"])
def handle_books():
    if request.method == "GET":
        return { "books": books}, 200
    if request.method == "POST":
        new_books = request.get_json()
        inserted_books = add_new_books(new_books, books)
        if inserted_books:
            return {"books": books, "message": "Success!"}, 201
        else:
            abort(404, message="Failed!")

# handling BOOkS related request/response
@app.get("/api/book/name/<string:title>")
def get_book_by_name(title):
    for book in books.values():
        if book["title"] == title:
            return {"book": book}, 200
    abort(404, message=f"Title '{title}' was NOT found in our library. \
        Please check the book's title and try again.")

@app.get("/api/book/id/<int:book_id>")
def get_book_by_id(book_id):
    book = books.get(book_id)
    if book:
        return {"book": book}, 200
    else:
        abort(400, message="Book not found!")

@app.route("/api/book", methods=["GET", "POST"])
def add_new_book():
    book_info = request.get_json()
    try:
        if book_info["title"]:
            book_id = len(books.keys()) + 1
            books[book_id] = book_info
            return {"book": books[book_id]}, 200
    except KeyError:
        abort(400, message="Operation failed. Could not add book to the library, \
                data provided is incomplete. Please check the title, author, \
                    and publisher, and try again")

@app.delete("/api/book/<string:book_id>")
def delete_book(book_id):
    id = int(id)
    try:
        book = books[id]
        message = {"message": f"Deleting book {books[id]["title"]} from library..."}
        del(books[id])
        return 
    except KeyError:
        return 
# handling MOVIES related request/response
@app.route("/api/movies/", methods=["GET", "POST"])
def handle_movies():
    if request.method == "GET":
        # TODO
        return { "movies": movies}
    if request.method == "POST":
        # TODO
        pass

# handling EVENTS related request/response
@app.route("/api/events", methods=["GET", "POST"])
def handle_events():
    if request.method == "POST":
        #TODO
        return {"message": "Received POST Request! Handle later..."}, 200
    else:
        #TODO
        return {"events": events}, 200
