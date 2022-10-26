from django.db import models


# Create your models here.

class Book(models.Model):
    cat_number = models.PositiveIntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    author_first_name = models.CharField(max_length=50)
    author_last_name = models.CharField(max_length=50)
    publish_year = models.PositiveIntegerField()
    publish_house = models.CharField(max_length=50)

class Reader(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    adress = models.CharField(max_length=200)
    document_number = models.CharField(max_length=40)

class Hire(models.Model):
    reader = Reader()
    book = Book()
