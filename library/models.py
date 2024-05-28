from django.db import models

class Publisher(models.Model):
    publisher_code = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)

class Book(models.Model):
    code = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    first_author = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    publisher_code = models.IntegerField()

    def __str__(self):
        return self.title
class Reader(models.Model):
    reader_code = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

class Loan(models.Model):
    loan_id = models.AutoField(primary_key=True)
    reader_code = models.IntegerField()
    book_code = models.IntegerField()
    loan_date = models.DateField()
    signature = models.CharField(max_length=255)

class Genre(models.Model):
    genre_code = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

class BookGenre(models.Model):
    book_code = models.IntegerField()
    genre_code = models.IntegerField()
    class Meta:
        unique_together = ('book_code', 'genre_code')

class OperationHistory(models.Model):
    operation_id = models.AutoField(primary_key=True)
    operation_date = models.DateField()
    operation_type = models.CharField(max_length=255)
    reader_code = models.IntegerField()
    book_code = models.IntegerField()