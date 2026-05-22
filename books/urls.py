from django.urls import path
from . import views

urlpatterns = [
    # This maps the URL to the view function we just wrote
    path('', views.book_list_api, name='book-list'),
    path('generic/', views.BookListCreate.as_view(), name='book-list-generic')
]
