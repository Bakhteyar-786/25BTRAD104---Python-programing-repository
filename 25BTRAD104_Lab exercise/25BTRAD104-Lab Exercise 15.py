# Lab Exercise 15: Library Management System
class Book:
    def __init__(self, book_id, title, author):
        self.book_id, self.title, self.author = book_id, title, author
        self.available = True

    def __str__(self):
        return f"[{self.book_id}] {self.title} by {self.author} - {'Available' if self.available else 'Issued'}"


class EBook(Book):  # Inheritance: EBook is a type of Book
    def __init__(self, book_id, title, author, size_mb):
        super().__init__(book_id, title, author)
        self.size_mb = size_mb

    def __str__(self):
        return super().__str__() + f" (E-Book, {self.size_mb} MB)"


class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book):
        self.books[book.book_id] = book

    def issue_book(self, book_id):
        book = self.books.get(book_id)
        if not book:
            print("Book not found.")
        elif not book.available:
            print(f"'{book.title}' is already issued.")
        else:
            book.available = False
            print(f"'{book.title}' issued successfully.")

    def return_book(self, book_id):
        book = self.books.get(book_id)
        if not book:
            print("Book not found.")
        elif book.available:
            print(f"'{book.title}' was not issued.")
        else:
            book.available = True
            print(f"'{book.title}' returned successfully.")

    def show_books(self):
        print(*self.books.values(), sep="\n")


# ---- Simulation / Testing ----
lib = Library()
lib.add_book(Book(1, "Python Basics", "A. Sharma"))
lib.add_book(EBook(2, "Learning AI", "S. Kumar", 5))
lib.issue_book(1)      # valid
lib.issue_book(1)      # already issued
lib.return_book(2)     # was not issued
lib.issue_book(9)      # not found
lib.show_books()