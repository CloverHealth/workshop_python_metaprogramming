class Bookshelf(object):

    def __init__(self):
        self._books = []

    def add_book(book):
        self._books.append(book)


def Bookshelf():

    bookshelf = object()
    bookshelf._books = []

    def add_book(book):
        bookshelf._books.append(book)
    bookshelf.add_book = add_book

    return bookshelf
