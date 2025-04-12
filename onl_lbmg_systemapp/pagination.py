from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Author,Book, BorrowRecord

def author_list(request):
    authors = Author.objects.all()  # Sabhi authors ko fetch karo
    paginator = Paginator(authors, 10)  # 10 authors per page
    page_number = request.GET.get('page')  # Page number ko GET parameter se le lo
    page_obj = paginator.get_page(page_number)
    return render(request, 'author_list.html', {'page_obj': page_obj})

def book_list(request):
    books = Book.objects.all()  # Sabhi books ko fetch karo
    paginator = Paginator(books, 10)  # 10 books per page
    page_number = request.GET.get('page')  # Page number ko GET parameter se le lo
    page_obj = paginator.get_page(page_number)
    return render(request, 'book_list.html', {'page_obj': page_obj})

def borrow_record_list(request):
    records = BorrowRecord.objects.all()  # Sabhi borrow records ko fetch karo
    paginator = Paginator(records, 10)  # 10 records per page
    page_number = request.GET.get('page')  # Page number ko GET parameter se le lo
    page_obj = paginator.get_page(page_number)
    return render(request, 'borrow_record_list.html', {'page_obj': page_obj})