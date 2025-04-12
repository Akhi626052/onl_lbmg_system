from django.shortcuts import render, redirect
from onl_lbmg_systemapp.forms import AuthorForm, BookForm, BorrowRecordForm
#pagination
from onl_lbmg_systemapp.models import Author, Book, BorrowRecord
from django.core.paginator import Paginator
from io import BytesIO
#admin access decorator
from django.contrib.auth.decorators import login_required, user_passes_test
import pandas as pd
from django.http import HttpResponse
def is_admin(user):
    return user.is_staff
@login_required
@user_passes_test(is_admin)
def dashboard_view(request):
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
    # Step 1: Authors data
    authors = Author.objects.all().values('id', 'name', 'email', 'bio')
    df_authors = pd.DataFrame(authors)

    # Step 2: Books data (related author name included)
    books = Book.objects.select_related('author').all()
    df_books = pd.DataFrame([{
        'id': book.id,
        'title': book.title,
        'genre': book.genre,
        'published_date': book.published_date,
        'author': book.author.name
    } for book in books])

    # Step 3: Borrow Records (related book title included)
    records = BorrowRecord.objects.select_related('book').all()
    df_borrow = pd.DataFrame([{
        'id': record.id,
        'user_name': record.user_name,
        'book': record.book.title,
        'borrow_date': record.borrow_date,
        'return_date': record.return_date
    } for record in records])

    # Step 4: Create Excel using BytesIO
    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df_authors.to_excel(writer, sheet_name='Authors', index=False)
        df_books.to_excel(writer, sheet_name='Books', index=False)
        df_borrow.to_excel(writer, sheet_name='BorrowRecords', index=False)

    # Step 5: Return Excel file in response
    output.seek(0)
    response = HttpResponse(
        output,
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=library_data.xlsx'
    return response




