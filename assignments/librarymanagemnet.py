class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        self.books.append({"title": title, "author": author})

    def search_book(self, keyword):
        found = False

        for book in self.books:
            if (book["title"].lower() == keyword.lower() or
                book["author"].lower() == keyword.lower()):
                print(f"Title : {book['title']}")
                print(f"Author: {book['author']}")
                found = True

        if not found:
            print("Book not found.")

    def display(self):
        for book in self.books:
            print(f"Title: {book['title']}, Author: {book['author']}")


library = Library()

library.add_book("Seto Dharti", "Amar Neupane")
library.add_book("Muna Madan", "Laxmi Prasad Devkota")
library.add_book("Palpasa Cafe", "Narayan Wagle")

print("All Books:")
library.display()

print("\nSearch by title:")
library.search_book("Seto Dharti")

print("\nSearch by author:")
library.search_book("Narayan Wagle")