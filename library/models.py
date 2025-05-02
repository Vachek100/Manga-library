from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Manga(models.Model):
    BORROWING_STATUS = [
        ('AVAILABLE', 'Available'),
        ('BORROWED', 'Borrowed'),
        ('RESERVED', 'Reserved'),
        ('LOST', 'Lost'),
        ('DAMAGED', 'Damaged'),
    ]

    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=10,
        choices=BORROWING_STATUS,
        default='AVAILABLE'
    )
    borrower = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True)
    borrow_date = models.DateField(blank=True, null=True)
    cover = models.ImageField(upload_to='covers/', blank=True, null=True)
    condition = models.CharField(max_length=100, blank=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} by {self.author.name} ({self.get_status_display()})"
