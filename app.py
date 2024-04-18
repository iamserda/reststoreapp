from flask import Flask, request

app = Flask("__name__")

inwood_library = {
    "books": [{"id": 1, "title": "1984", "author": "George Orwell", "publisher": "Penguin"}],
    "movies": [],
    "events": [],
    }

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
        return { "books": inwood_library["books"]}, 200
    if request.method == "POST":
        new_books = request.get_json()
        inserted_books = add_new_books(new_books, inwood_library)
        if inserted_books:
            return {"books": inwood_library["books"], "message": "Success!"}, 201
        else:
            return {"message": "Failed!", "books": inwood_library["books"]}, 404

# handling BOOkS related request/response
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

# handling MOVIES related request/response
@app.get("/api/movies/")
def get_movies():
    return { "movies": inwood_library["movies"]}

# handling EVENTS related request/response
@app.route("/api/events", methods=["GET", "POST"])
def handle_events():
    if request.method == "POST":
        #TODO
        return {"message": "Received POST Request! Handle later..."}
    else:
        #TODO
        return {"events": inwood_library["events"]}

# Helpers, TODO: move these to some directory
def add_new_books(books:list, book_list:list):
        if not books:
            return False
        for book in books:
            count = len(book_list["books"])
            new_book = {"id": count + 1}
            for k, v in book.items():
                new_book[k] = v
            print(new_book)
            book_list["books"].append(new_book)
        return True