import types

# This is the Bookshelf class
# Except we're doing it with `class:`
class BookshelfAsClass(object):

    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)


# This is the Bookshelf class
# Except we're doing it with `def`
def BookshelfAsFunction():

    # __new__
    bookshelf = types.SimpleNamespace()

    # __init__
    bookshelf._books = []

    # sugar - add the function
    def add_book(book):
        bookshelf._books.append(book)
    bookshelf.add_book = add_book

    return bookshelf
