from django.shortcuts import render, redirect
from onl_lbmg_systemapp.forms import AuthorForm, BookForm, BorrowRecordForm
#pagination
from onl_lbmg_systemapp.models import Author, Book, BorrowRecord
from django.core.paginator import Paginator

#admin access decorator
from django.contrib.auth.decorators import login_required, user_passes_test
#excel file dependenci
import pandas as pd
from io import BytesIO
from django.http import HttpResponse
#logout
from django.contrib.auth import logout
def is_admin(user):
    return user.is_staff#built-in property
@login_required
@user_passes_test(is_admin)
def dashboard_view(request):
    return render(request, 'dashboard.html')

def custom_logout(request):
    logout(request)
    return redirect('dashboard')

#deshboard publish
def dashboard_public(request):
    return render(request, 'dashboard.html')

# pagination
def author_list(request):
    authors = Author.objects.all()
    paginator = Paginator(authors, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'library/list_pages/author_list.html', {'page_obj': page_obj})

def book_list(request):
    books = Book.objects.all()
    paginator = Paginator(books, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'library/list_pages/book_list.html', {'page_obj': page_obj})

def borrow_record_list(request):
    records = BorrowRecord.objects.all()
    paginator = Paginator(records, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'library/list_pages/borrow_record_list.html', {'page_obj': page_obj})


#excel-Emport
def export_to_excel(request):
    # Authors data
    authors = Author.objects.all().values('id', 'name', 'email', 'bio')
    df_authors = pd.DataFrame(authors)
    
    #Books data Fetch (related author name included)
    books = Book.objects.select_related('author').all()
    df_books = pd.DataFrame([{
        'id': book.id,
        'title': book.title,
        'genre': book.genre,
        'published_date': book.published_date,
        'author': book.author.name
    } for book in books])

    # Borrow Records (related book title included)
    records = BorrowRecord.objects.select_related('book').all()
    df_borrow = pd.DataFrame([{
        'id': record.id,
        'user_name': record.user_name,
        'book': record.book.title,
        'borrow_date': record.borrow_date,
        'return_date': record.return_date
    } for record in records])

    # Create Excel using BytesIO
    output = BytesIO() # temporary file
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df_authors.to_excel(writer, sheet_name='Authors', index=False)
        df_books.to_excel(writer, sheet_name='Books', index=False)
        df_borrow.to_excel(writer, sheet_name='BorrowRecords', index=False)

    # Return Excel file in response
    output.seek(0)
    response = HttpResponse(
        output,
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=library_data.xlsx'
    return response



