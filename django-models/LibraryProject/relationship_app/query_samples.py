from relationship_app.models import Author, Book, Library, Librarian


# 2. List all books in a library
library = Library.objects.get(name="National Library")
Library.objects.get(name="city_library")
library_books = library.books.all()
print(library_books)
# for book in books_in_library:
#     print(book.title)

# 1. Query all books by a specific author
author = Author.objects.get(name="Chinua Achebe")
books_by_author = Book.objects.filter(author=author)
print("Books by Chinua Achebe:")
for book in books_by_author:
    print(book.title)


# 3. Retrieve the librarian for a library
librarian = Librarian.objects.get(library=library)
print(f"Librarian for {library.name}: {librarian.name}")