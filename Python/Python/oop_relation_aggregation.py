# Aggregation: Aggregation is a specialized form of  association, where one class represents a "whole" 
# and another class represents a "part." The part  class can exist independently of the whole class. 
# It is represented by a diamond-shaped arrow  pointing from the part class to the whole class.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self ,book):
        self.books.append(book)

    def display(self):
        print(f"Books in {self.name} library:")
        for i in self.books:

            print(i.title, i.author)

book1 = Book("Python Crash Course", "Eric Matthes")
book2 = Book("Clean Code", "Robert C. Martin")
book3 = Book("The Pragmatic Programmer", "Andrew Hunt, David Thomas")


library = Library("maidi library ha")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.display()

