from django.urls import path
from .views import user_list, book_list, book_detail

urlpatterns = [
    path('users/', user_list),
    path('books/', book_list, name='book-list'),
    path('books/<uuid:pk>/', book_detail, name='book-detail'),  # UUID in URL
]