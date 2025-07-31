from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length= 200, null=True, blank=True)

    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length= 200, null=True, blank=True)
    author = models.ForeignKey(Author, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Library(models.Model):
    name = models.CharField(max_length= 200, null=True, blank=True)
    books = models.ManyToManyField(Book, null=True)

    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length= 200)
    library = models.OneToOneField(Library, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name