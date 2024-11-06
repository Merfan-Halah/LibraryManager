from Library import Library


def main():
    library = Library()
    library.loadFromFile("library.txt")

    while True:
        print("=== Library Manager ===")
        print("1. Add Book")
        print("2. List All Books")
        print("3. Search Books")
        print("4. Borrow/Return Book")
        print("5. Save and Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author: ")
            year = input("Enter publication year: ")

            library.addBook(title, author, year)

            print("Book was added")
        elif choice == '2':
            library.allBooks()
        elif choice == '3':
            search_term = input("Enter book title or author name: ")
            library.searchBook(search_term)
        elif choice == '4':
            title = input("Enter the book title: ")
            action = input("Type 'borrow' to borrow or 'return' to return a book: ")
            if action.lower() == 'borrow':
                library.borrowBook(title)
            elif action.lower() == 'return':
                library.returnBook(title)
            else:
                print("Invalid action.")
        elif choice == '5':
            library.saveToFile()
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
