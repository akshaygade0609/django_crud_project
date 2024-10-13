from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)  # Title of the book
    author = models.CharField(max_length=100)  # Author's name
    description = models.TextField()  # Description of the book
    published_date = models.DateField()  # Publication date

    def __str__(self):
        return self.title
