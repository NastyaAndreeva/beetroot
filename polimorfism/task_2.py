# All 3 classes must have a readable __repr__ and __str__ methods.
# __str__(self): Returns a string representation of the object. Used when you use the str() function or print() to display the object.

# __repr__(self): Returns a string representation of the object, mainly used for debugging. It is used when you use the repr() function.

class Author:
    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []
        
class Book:
    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []
        self.total_books = 0

    def new_book(self, name: str, year: int, author):
        book = Book(name, year, author)
        self.books.append(book)
        self.total_books += 1
        return book
    
    def group_by_author(self, author):
        sorted_books = []
        for book in self.books:
            if book.author == author:
                sorted_books.append(book)

        return sorted_books

    def group_by_year(self, year):
        sorted_books = []
        for book in self.books:
            if book.year == year:
                sorted_books.append(book)

        return sorted_books

library_1 = Library("Library 1")
author_1 = Author("Luiza Hay", "The US", 1940)
library_1.new_book("Life loves you", 2010, author_1)
print(library_1.total_books)
print(library_1.books)


