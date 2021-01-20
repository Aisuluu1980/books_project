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


def delete(request, id):
    book = Books.objects.get(id=id)
    book.delete()
    return redirect(books)


def mark_book(request, id):
    book = Books.objects.get(id=id)
    book.is_favorite = True
    book.save()
    return redirect(books)


def unmark_book(request, id):
    book = Books.objects.get(id=id)
    book.is_favorite = False
    book.save()
    return redirect(books)


def detail_book(request, id):
    book = Books.objects.get(id=id)
    return render(request, 'book_detail.html', context={'book': book})
