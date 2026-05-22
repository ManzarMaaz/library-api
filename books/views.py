from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookListCreate(generics.CreateAPIView):
    queryset = Book.objects.select_related('author').all()
    serializer_class = BookSerializer

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.select_related('author').all()
    serializer_class = BookSerializer

# Create your views here.
@api_view(['GET'])
def book_list_api(request):
    """API endpoint to return a list of books in JSON format."""

    books = Book.objects.select_related('author').all()

    serializer = BookSerializer(books, many=True)

    return Response(serializer.data)
