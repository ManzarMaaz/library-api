from django.urls import path
from . import views

urlpatterns = [
    # The Books endpoints
    path('books/', views.BookListCreate.as_view(), name='book-list'),
    path('books/<int:pk>/', views.BookDetail.as_view(), name='book-detail-generic'),

    # The Authors endpoints
    path('authors/', views.AuthorListCreate.as_view(), name='author-list'),
    path('authors/<int:pk>/', views.AuthorDetail.as_view(), name='author-detail'),
]
