class Library:
    def __init__(self, name):
        self.name = name
        self.authors = []
        self.books = []

    def new_book(self, name: str, year: int, author):
        book = Book(name, year, author)
        self.books.append(book)
        Book.amount_of_books += 1

    def group_by_author(self, author):
        sorted_by_author_books = []
        for book in self.books:
            if book.author.lower() == author.lower():
                sorted_by_author_books.append(book)

        return sorted_by_author_books

    def group_by_year(self, year):
        sorted_by_year_books = []
        for book in self.books:
            if book.year == year:
                sorted_by_year_books.append(book)

        return sorted_by_year_books

    def __str__(self): 
        return str(self.name)

    def __repr__(self): 
        return str(self.name)

class Book:
    amount_of_books = 0
    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author 

    def __str__(self): 
        return str(f"Name: {self.name}, year: {self.year}, author: {self.author}")

    def __repr__(self): 
        return str(f"Name: {self.name}, year: {self.year}, author: {self.author}")

class Author:
    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []

    def __str__(self): 
        return str(f"Name: {self.name}, country: {self.country}, birthday: {self.birthday}, books: {self.books}")

    def __repr__(self): 
        return str(f"Name: {self.name}, country: {self.country}, birthday: {self.birthday}, books: {self.books}")

library_1 = Library("Self-development")
author_1 = Author("Brian Traicy", "The US", 1952)
author_2 = Author("Luiza Hay", "The US", 1948)

library_1.new_book("Eat that frog", 2002, author_1)
library_1.new_book("Life loves you", 2017, author_2)
print(library_1.books)