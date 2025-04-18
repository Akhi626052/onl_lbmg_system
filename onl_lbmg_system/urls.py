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
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('', views.dashboard_public, name='dashboard_public'),
    path('logout/', views.custom_logout, name='custom_logout'),
    #all logout redirect deshboard
    path('admin/logout/', views.custom_logout),  #override default admin logout
    
    
    
]
