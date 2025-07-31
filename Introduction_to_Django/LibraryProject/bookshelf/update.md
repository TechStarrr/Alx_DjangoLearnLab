<!--  Update Book Entry -->

```python
from library.models import Book  # Replace 'library' with your actual app name
book = Book.objects.get(id=1)
book.title = "Nineteen Eighty-Four"
book.save()

print(book)