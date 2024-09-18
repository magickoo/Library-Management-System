from django.shortcuts import render

# Create your views here.
from rest_framework import APIView
from rest_framework import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class Home(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self,request):
        content = {'message': 'Hello, World!'}
        return Response(content)
    
    