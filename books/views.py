from django.shortcuts import render
from django.http import JsonResponse
from .models import Book

# Create your views here.
def book_list_api(request):
    """API endpoint to return a list of books in JSON format."""

    books = Book.objects.select_related('author').all()

    data = []
    for book in books:
        data.append({
            "title": book.title,
            "isbn": book.isbn,
            "author": book.author.name, # No extra DB hit because of select_related!
            "published_date": book.published_date.strftime('%Y-%m-%d') if book.published_date else None
        })

    return JsonResponse({"status": "success", "data": data})
