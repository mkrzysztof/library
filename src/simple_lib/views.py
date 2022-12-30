from django.db import IntegrityError
from django.shortcuts import (render, redirect)
from django.urls import reverse
from django.views.generic import ListView
from django.views import View
from .models import (Book, Reader, Hire)
from .forms import ReaderNumberForm, BookNumberForm

# Create your views here.
class BookListView(ListView):
    model = Book
    context_object_name = 'my_books'

class HireIndexView(View):
    """Wyszukanie numeru karty bibliotecznej czytenika"""

    def get(self, request):
        ctx = { 'reader_number': ReaderNumberForm() }
        return render(request, 'simple_lib/hire_index.html', context=ctx)

    
class FindReaderView(View):
    def post(self, request):
        """
        Znajduje czytelnika według karty bibliotecznej
        """
        form = ReaderNumberForm(request.POST)
        if form.is_valid():
            reader_number = form.cleaned_data['number']
            try:
                reader = Reader.objects.get(pk=reader_number)
                print(reader)
                request.session['reader_number'] = reader_number
            except Reader.DoesNotExist:
                reader = None
        return redirect(reverse('borrow-book'))


class BorrowBookView(View):
    def get(self, request):
        request.session['book_hire'] = False
        ctx = {'book_number': BookNumberForm(),
               'reader_number': request.session['reader_number']}
        return render(request, 'simple_lib/borrow_book.html', context=ctx)

    def post(self, request):
        form = BookNumberForm(request.POST)
        if form.is_valid():
            book_number = form.cleaned_data['number']
            reader_number = request.session['reader_number']
            book = Book.objects.get(pk=book_number)
            reader = Reader.objects.get(pk=reader_number)
            try:
                hire = Hire.objects.create(reader=reader, book=book)
                hire.save()
            except IntegrityError:
                print('powtórzenie')
                request.session['book_hire'] = True
            else:
                request.session['book_hire'] = False
        return redirect(reverse('borrow-book'))

    
class StartSiteView(View):
    def get(self, request):
        return render(request, 'simple_lib/start_site.html')



class ReturnBookView(View):
    """Oddanie książki niezależnie kto ją przyniósł"""
    def get(self, request):
        ctx = {'book_number': BookNumberForm()}
        return render(request, 'simple_lib/return_book.html', context=ctx)

    def post(self, request):
        form = BookNumberForm(request.POST)
        if form.is_valid():
            book_number = form.cleaned_data['number']
            book = Book.objects.get(pk=book_number)
            hire = Hire.objects.filter(book=book)
            hire.delete()
        return redirect(reverse('return-book'))


class HiringBookView(ListView)
