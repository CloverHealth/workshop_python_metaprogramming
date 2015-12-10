# This is the Bookshelf class
# Except we're doing it with `class:`
class BookshelfAsClass(object):

    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)


# This is the Bookshelf class
# Except we're doing it with `type()`

def bookshelf_init(self):
    self._books = []

def bookshelf_add_book(self, book):
    self._books.append(book)

BookshelfAsType = type('BookshelfAsType', (object,), {
    '__init__': bookshelf_init,
    'add_book': bookshelf_add_book,
})
