class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        for index in range(len(self.books)):
            if (
                self.books[index].title == book.title
                and self.books[index].author == book.author
            ):
                del self.books[index]
                break

    def search_books(self, search_string):
        result = []
        search_string = search_string.lower()
        for book in self.books:
            if (
                search_string in book.title.lower()
                or search_string in book.author.lower()
            ):
                result.append(book)
        return result


# Testing Library: Lane's Library
# Adding book The Great Gatsby by F. Scott Fitzgerald
# Adding book Pride and Prejudice by Jane Austen
# Adding book The Lord of the Rings by J.R.R. Tolkien
# Adding book Great Expectations by Charles Dickens
# Adding book To Kill a Mockingbird by Harper Lee
# Removing book The Great Gatsby by F. Scott Fitzgerald
# Error: list index out of range
