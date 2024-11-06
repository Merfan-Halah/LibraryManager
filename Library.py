from Book import Book
import json


class Library:

    def __init__(self):
        self.bookList = []

    def addBook(self, title, author, year):
        b = Book(title, author, year)
        self.bookList.append(b)

    def allBooks(self):
        for book in self.bookList:
            print(book)

    def borrowBook(self, title):
        borrowed = False
        for book in self.bookList:
            if book.title == title and book.status == "Available":
                book.status = "Borrowed"
                borrowed = True
        if borrowed:
            print(f"You borrowed {title}")
        else:
            print("Book is not available")

    def returnBook(self, title):
        available = False
        for book in self.bookList:
            if book.title == title and book.status == "Borrowed":
                book.status = "Available"
                available = True
        if available:
            print(f"You returned {title}")
        else:
            print("Book was not borrowed")

    def searchBook(self, input):
        for book in self.bookList:
            if book.title == input or book.author == input:
                print(book)

    def saveToFile(self, filename="library.txt"):
        with open(filename, 'w') as f:
            json_data = [{'title': book.title, 'author': book.author, 'year': book.year, 'status': book.status} for book
                         in self.bookList]
            json.dump(json_data, f)
        print("Library data saved.")

    def loadFromFile(self, filename="library.txt"):
        try:
            with open(filename, 'r') as f:
                json_data = json.load(f)
                self.bookList = [Book(book['title'], book['author'], book['year'], book['status']) for book in
                                 json_data]
            print("Library data loaded.")
        except FileNotFoundError:
            print("No previous library data found")
        except Exception as e:
            print(f"Error loading library data: {e}")
