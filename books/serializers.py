from rest_framework import serializers
from .models import Book, Author


class BookSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='name',
        queryset=Author.objects.all()
    )

    class Meta:
        model = Book
        fields = ['url', 'title', 'isbn', 'author', 'published_date']
        extra_kwargs = {
            'url': {'view_name': 'book-detail-generic', 'lookup_field': 'pk'}
        }
