# library_management.py
# Define the Book class

class Book:
    # Constructor to initialize a book with title and author
    def __init__(self, title, author):
        self.title = title  # Public attribute for the book title
        self.author = author  # Public attribute for the author name
        self._is_checked_out = False  # Private attribute to track if the book is checked out

    # Method to check out the book (if it's available)
    def check_out(self):
        if not self._is_checked_out:  # If the book is not already checked out
            self._is_checked_out = True  # Mark it as checked out
            return True  # Return True to indicate success
        return False  # Return False if the book was already checked out

    # Method to return the book (if it was checked out)
    def return_book(self):
        if self._is_checked_out:  # If the book was checked out
            self._is_checked_out = False  # Mark it as available
            return True  # Return True to indicate success
        return False  # Return False if the book was not checked out

    # Method to check if the book is available
    def is_available(self):
        return not self._is_checked_out  # Return True if the book is available


# Define the Library class
class Library:
    # Constructor to initialize an empty list of books
    def __init__(self):
        self._books = []  # Private list to store all books in the library

    # Method to add a new book to the library
    def add_book(self, book):
        self._books.append(book)  # Add the book to the library list

    # Method to check out a book by its title
    def check_out_book(self, title):
        for book in self._books:  # Loop through all books in the library
            if book.title == title:  # Find the book with the matching title
                if book.check_out():  # Try to check it out
                    print(f"'{title}' has been checked out.")
                    return
                else:
                    print(f"'{title}' is already checked out.")
                    return
        print(f"'{title}' not found in the library.")  # If no matching book is found

    # Method to return a book by its title
    def return_book(self, title):
        for book in self._books:  # Loop through all books in the library
            if book.title == title:  # Find the book with the matching title
                if book.return_book():  # Try to return it
                    print(f"'{title}' has been returned.")
                    return
                else:
                    print(f"'{title}' was not checked out.")
                    return
        print(f"'{title}' not found in the library.")  # If no matching book is found

    # Method to list all available books in the library
    def list_available_books(self):
        available_books = [book for book in self._books if book.is_available()]  # Get all available books
        if available_books:  # If there are any available books
            for book in available_books:  # Print each available book
                print(f"{book.title} by {book.author}")
        else:
            print("No books are currently available.")  # If no books are available
