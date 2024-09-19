from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework import APIView
from rest_framework import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from book.models import Book
from book.serializers import BookSerializer
class Home(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self,request):
        content = {'message': 'Hello, World!'}
        return Response(content)
    
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    
    
    