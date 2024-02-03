from django.shortcuts import render
from django.views.generic import ListView, CreateView

from .models import Book

# Create your views here.

class BookListView(ListView):
    model = Book
    template_name = 'book/index.html'
    context_object_name = 'books'


class BookCreateView(CreateView):
    model = Book
    template_name = 'book/create.html'
    fields = ['name', 'image', 'rating', 'genre']
    