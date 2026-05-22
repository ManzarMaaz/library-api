from django.urls import path
from . import views

urlpatterns = [
    # The main List/Create endpoint
    path('', views.BookListCreate.as_view(), name='book-list'),

    # The Retrieve/Update/Destroy endpoint (Notice the name matches what you put in serializers.py!)
    path('<int:pk>/', views.BookDetail.as_view(), name='book-detail-generic')
]
