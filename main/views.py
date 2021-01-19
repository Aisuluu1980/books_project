from django.shortcuts import render, redirect
from .models import Books

# Create your views here.


def books(request):
    books_list = Books.objects.all()
    return render(request, 'books.html', {"books_list": books_list})


def add_books(request):
    form = request.POST
    title = form['title']
    subtitle = form['subtitle']
    description = form['description']
    genre = form['genre']
    price = form['price']
    author = form['author']
    year = form['year']

    book = Books(title=title, subtitle=subtitle, description=description, genre=genre,
                 price=price, author=author, year=year)
    book.save()
    return redirect(books)
