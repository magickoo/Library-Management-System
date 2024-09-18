from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return self.name

class Book(models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('borrowed', 'Borrowed'),
    ]
    
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publication_year = models.PositiveIntegerField(default="0000")
    category = models.CharField(max_length=255,default="Uncategorized")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')

    def __str__(self):
        return self.title
