from django.contrib import admin # type: ignore
from django.urls import path # type: ignore
from onl_lbmg_systemapp import views
urlpatterns = [

    path('admin/', admin.site.urls),
    #path('onlinedm/', views.onlinedm, name='onlinedm'),
    #list 
    path('authors/', views.author_list, name='author_list'),
    path('books/', views.book_list, name='book_list'),
    path('borrow-records/', views.borrow_record_list, name='borrow_record_list'),
    
    path('export-excel/', views.export_to_excel, name='export_excel'),
    path('', views.dashboard_view, name='dashboard'),
]
