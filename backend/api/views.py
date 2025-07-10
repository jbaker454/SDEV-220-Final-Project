from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, viewsets
from .models import User, Product
from .serializers import UserSerializer, BookSerializer, ProductSerializer
from django.shortcuts import get_object_or_404

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

@api_view(['GET', 'POST'])
def user_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'POST'])
def book_list(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    serializer = BookSerializer(book)
    return Response(serializer.data)