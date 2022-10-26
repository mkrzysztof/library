from django.shortcuts import (render, redirect)
from django.urls import reverse
from django.views.generic import ListView
from django.views import View
from .models import (Book, Reader, Hire)
from .forms import ReaderNumberForm

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
        return redirect(reverse('hiring'))

    
class EndOfServiceView(View):
    def get(self, request):
        del(request.session['reader_number'])
        return redirect(reverse('hiring'))
