<!--  Create Book Entry -->

```python
from library.models import Book  # Replace 'library' with your actual app name
book = Book.objects.create(title="1984", author="George Orwell", published_year=1949)
print(book)