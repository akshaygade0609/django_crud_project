from django.urls import path
from . import views
from .views import register_page, login_page, logout_view

urlpatterns = [
    path('', views.book_list, name='book_list'),  # List all books
    path('book/<int:pk>/', views.book_detail, name='book_detail'),  # Book details
    path('book/new/', views.book_create, name='book_create'),  # Create new book
    path('book/<int:pk>/edit/', views.book_update, name='book_update'),  # Update book
    path('book/<int:pk>/delete/', views.book_delete, name='book_delete'),  # Delete book
    path('register/', register_page, name='register_page'),
    path('login/', login_page, name='login_page'),
    path('logout/', logout_view, name='logout'),
]
