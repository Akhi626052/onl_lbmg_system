from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    bio = models.TextField()

class Book(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    published_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

class BorrowRecord(models.Model):
    user_name = models.CharField(max_length=100)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateField()
    return_date = models.DateField()

#Username: akhilesh
#Email: akhilesh@gmail.com
#Password: 123456