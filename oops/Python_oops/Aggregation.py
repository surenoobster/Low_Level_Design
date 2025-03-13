class Book:
    def __init__(self, title):
        self.title = title

class Library:
    def __init__(self, book):
        self.book = book  # Aggregation (Library has-a Book)

    def show_book(self ,book):
        print(f"Library has book: {self.book.title}")

my_book = Book("Python Programming")
my_library = Library(my_book)
my_library.show_book(my_book)



#or

class Book:
    def __init__(self, title):
        self.title = title

class Library:
    def __init__(self, book):
        self.book = book  # Aggregation (Library has-a Book)

    def show_book(self):
        print(f"Library has book: {self.book.title}")

my_book = Book("Python Programming")
my_library = Library(my_book)
my_library.show_book()

