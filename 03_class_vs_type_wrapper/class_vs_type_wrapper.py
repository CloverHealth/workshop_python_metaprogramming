class Bookshelf(object):

    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)


def bookshelf_init(self):
    self._books = []

def bookshelf_add_book(self, book):
    self._books.append(book)

Bookshelf = type('Bookshelf', (object,), {
    '__init__': bookshelf_init,
    'add_book': bookshelf_add_book,
})
