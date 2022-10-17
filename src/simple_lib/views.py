from django.shortcuts import render
from django.views.generic import ListView
from .models import (Book, Borrower, Hire)

# Create your views here.
class BookListView(ListView):
    model = Book
    context_object_name = 'my_books'
