<!--  Delete Book Entry -->

```python

from bookshelf.models import Book 
book = Book.objects.get(title="Nineteen Eighty-Four")
book = Book.objects.get(author = "George Orwell")
book = Book.objects.get(published_year = "1949")
book.delete()

print(book.title)
print(book.author)
print(book.published_year)
print(Book.objects.all())


