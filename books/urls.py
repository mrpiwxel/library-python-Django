from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('books/list/', views.book_list, name='book_list'),
    path('book/add/', views.add_book, name='add_book'),
    path('book/<int:book_id>/', views.show_book, name='showbook'),
    path('book/<int:book_id>/edit/', views.edit_book, name='edit_book'),
    path('books/change-status/', views.edit_status_book_page, name='edit_status_book_page'),
    path('book/<int:book_id>/change-status/', views.edit_status_book, name='edit_status_book'),
    path('book/<int:book_id>/delete/', views.delete_book, name='delete_book'),
    path('books/borrow/', views.borrowing_page, name='borrowing_page'),
    path('books/borrowlist/', views.borrowlist, name='borrowlist'),
    path('book/<int:book_id>/borrow/', views.borrow_book, name='borrow_book'),
    path('book/<int:book_id>/return/', views.return_book, name='return_book'),

    
]
