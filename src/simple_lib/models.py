from django.db import models


# Create your models here.
class Reader(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    adress = models.CharField(max_length=200)
    document_number = models.CharField(max_length=40)

class Book(models.Model):
    cat_number = models.PositiveIntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    author_first_name = models.CharField(max_length=50)
    author_last_name = models.CharField(max_length=50)
    publish_year = models.PositiveIntegerField()
    publish_house = models.CharField(max_length=50)


class Hire(models.Model):
    reader = models.ForeignKey(Reader, null=False,
                               on_delete=models.PROTECT)
    book = models.ForeignKey(Book, unique=True, null=False,
                             on_delete=models.PROTECT)
