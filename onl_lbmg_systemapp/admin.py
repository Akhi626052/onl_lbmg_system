from django.contrib import admin

from onl_lbmg_systemapp.models import Author, Book, BorrowRecord

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(BorrowRecord)