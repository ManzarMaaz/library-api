from rest_framework import serializers
from .models import Book, Author


class BookSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='name',
        queryset=Author.objects.all()
    )

    class Meta:
        model = Book
        fields = ['id', 'title', 'isbn', 'author', 'published_date']
