from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Manga(models.Model):
    BORROWING_STATUS = [
        ('AVAILABLE', 'Available'),
        ('BORROWED', 'Borrowed'),
        ('RESERVED', 'Reserved'),
    ]

    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=10,
        choices=BORROWING_STATUS,
        default='AVAILABLE'
    )
    borrower = models.CharField(max_length=100, blank=True, null=True)
    borrow_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} by {self.author.name} ({self.get_status_display()})"
