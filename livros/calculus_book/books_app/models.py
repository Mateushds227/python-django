from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cover_image = models.ImageField(upload_to='book_covers/')
    description = models.TextField()
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.title
