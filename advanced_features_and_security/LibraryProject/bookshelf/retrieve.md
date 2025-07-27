<!--  Retrieve Book Entry -->

```python
from library.models import Book  # Replace 'library' with your actual app name
book = Book.objects.all()
book = Book.objects.get(title="1984")
book = Book.objects.get(author = "George Orwell")
book = Book.objects.get(published_year = "1949")

print(book.title)
print(book.author)
print(book.published_year)
print(book)
