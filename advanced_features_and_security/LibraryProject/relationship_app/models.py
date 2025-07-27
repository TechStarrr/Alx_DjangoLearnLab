from django.db import models
from .managers import CustomUserManager
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    objects = CustomUserManager()  # Link to custom manager

    def __str__(self):
        return self.username


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
    
    class Meta:
        permissions = [
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"),
        ]
    

#Setting up ROLE BASED VIEWS
class UserProfile(models.Model):
    ROLE_CHOICES = (
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    )

    user = models.OneToOneField(AbstractUser, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f'{self.user.username} - {self.role}'
    
    

