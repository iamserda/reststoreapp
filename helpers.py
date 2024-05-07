# Helpers, TODO: move these to some directory
def add_new_books(new_books:list, books_dict):
    if not new_books:
        return False
    for book in new_books:
        book_id = len(books_dict.keys()) + 1
        books_dict[book_id] = book
    return True
