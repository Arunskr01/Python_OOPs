import pickle

class Books:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True
    
    def __str__(self):
        if self.available:
            status = "Available"
        else:
            status = "Borrowed"
        return f"{self.title} by {self.author}, ISBN: {self.isbn}, Status: {status}"
    
class Library:
    def __init__(self):
        self.books = []
    
    def add_books(self,book):
        self.books.append(book)
        
    def borrow_books(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                book.available = False
                print(f"You have borrowed '{book.title}'")
                print("")
                return
        print("Book not found")
        
    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                book.available = True
                print(f"You've returned {book.title}")
                print("")
                return
        print("Book not found")
        
    def display_books(self):
        if not self.books:
            print("Library is empty")
            print("")
        else:
            for book in self.books:
                print(book)
    
    def save_library(self, filename = "lib.pkl"):
        with open(filename, 'wb') as f:
            pickle.dump(self, f)

    def load_library(self):
        with open("lib.pkl", 'rb') as f:
            return pickle.load(f)

book1 = Books("The Great Gatsby", "F. Scott Fitzgerald", "111")
book2 = Books("To Kill a Mockingbird", "Harper Lee", "333")
library = Library()
library.add_books(book1)
library.add_books(book2)
library.borrow_books("111")
library.save_library()
library.load_library()
library.display_books()
