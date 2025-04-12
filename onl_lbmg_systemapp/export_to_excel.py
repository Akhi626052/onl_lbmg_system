# from django.http import HttpResponse
# from openpyxl import Workbook
# from onl_lbmg_systemapp.models import Author, Book, BorrowRecord

# def export_to_excel(request):
#     # Create a workbook and add sheets
#     wb = Workbook()
#     ws1 = wb.active
#     ws1.title = 'Authors'
    
#     # Add author data to the sheet
#     authors = Author.objects.all()
#     ws1.append(['ID', 'Name', 'Email', 'Bio'])
#     for author in authors:
#         ws1.append([author.id, author.name, author.email, author.bio])
    
#     # Add books data
#     ws2 = wb.create_sheet(title='Books')
#     books = Book.objects.all()
#     ws2.append(['ID', 'Title', 'Genre', 'Published Date', 'Author'])
#     for book in books:
#         ws2.append([book.id, book.title, book.genre, book.published_date, book.author.name])
    
#     # Add borrow records data
#     ws3 = wb.create_sheet(title='Borrow Records')
#     records = BorrowRecord.objects.all()
#     ws3.append(['ID', 'User Name', 'Book', 'Borrow Date', 'Return Date'])
#     for record in records:
#         ws3.append([record.id, record.user_name, record.book.title, record.borrow_date, record.return_date])

#     # Save the workbook as an HTTP response
#     response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
#     response['Content-Disposition'] = 'attachment; filename="library_data.xlsx"'
#     wb.save(response)
#     return response
