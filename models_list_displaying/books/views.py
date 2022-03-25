from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from books.models import Book


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'books/books_list.html'
    context = {'books': Book.objects.values()}
    return render(request, template, context)


dates = [date['slug'] for date in Book.objects.values('slug').distinct('pub_date').order_by('pub_date')]


def show_book(request, slug):
    template = 'books/books_by_date.html'
    books = Book.objects.filter(slug=slug, pub_date=slug)
    page_number = dates.index(slug) + 1
    paginator = Paginator(dates, 1)
    page = paginator.get_page(page_number)
    if page.has_previous():
        prev_page = paginator.get_page(page.previous_page_number())[0]
    else:
        prev_page = 0
    if page.has_next():
        next_page = paginator.get_page(page.next_page_number())[0]
    else:
        next_page = 0
    context = {'books': books,
               'prev_page': prev_page,
               'next_page': next_page}
    return render(request, template, context)
