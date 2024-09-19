from django.urls import path, include
from .views import Home
from rest_framework import routers
from django import views

router = routers.DefaultRouter()
router.register(r'books',views.BookViewSet,basename = 'book')
urlpatterns = [
    path('', include(router.urls)),
]

