from relationship_app.models import Author 
from relationship_app.models import Book
from relationship_app.models import Library
from relationship_app.models import Librarian


# 2. List all books in a library
library_name = "Central Library"  # Or whatever name you're searching
library = Library.objects.get(name=library_name)
library.books.all()
print(library)

def get_library_by_name(library_name):
    try:
        library = Library.objects.get(name=library_name)
        print("Library found:", library)
    except Library.DoesNotExist:
        print("Library not found.")


# 1. Query all books by a specific author
author_name = "Chinua Achebe"
author = Author.objects.get(name= author_name)
Book.objects.filter(author=author)

def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        return books
    except Author.DoesNotExist:
        print(f"No author found with name: {author_name}")
        return []



# 3. Retrieve the librarian for a library
librarian_name = "Okafor chinyere"
librarian = Librarian.objects.get(librarian=librarian_name)
print(f"Librarian for {library.name}: {librarian.name}")