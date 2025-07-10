from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import user_list, book_list, book_detail, ProductViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Include the router's URLs
    path('users/', user_list),
    path('books/', book_list, name='book-list'),
    path('books/<uuid:pk>/', book_detail, name='book-detail'),  # UUID in URL
]