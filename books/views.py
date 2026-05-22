from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookListCreate(generics.ListCreateAPIView):
    queryset = Book.objects.select_related('author').all()
    serializer_class = BookSerializer

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.select_related('author').all()
    serializer_class = BookSerializer
