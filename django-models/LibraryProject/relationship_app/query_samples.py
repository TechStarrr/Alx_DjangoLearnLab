from relationship_app.models import Author 
from relationship_app.models import Book
from relationship_app.models import Library
from relationship_app.models import Librarian


# 2. List all books in a library
library_name = "Central Library"  # Or whatever name you're searching
library = Library.objects.get(name=library_name)
print(library)

def get_library_by_name(library_name):
    try:
        library = Library.objects.get(name=library_name)
        print("Library found:", library)
    except Library.DoesNotExist:
        print("Library not found.")


# 1. Query all books by a specific author
author = Author.objects.get(name="Chinua Achebe")
books_by_author = Book.objects.filter(author=author)
print("Books by Chinua Achebe:")
for book in books_by_author:
    print(book.title)


# 3. Retrieve the librarian for a library
librarian = Librarian.objects.get(library=library)
print(f"Librarian for {library.name}: {librarian.name}")