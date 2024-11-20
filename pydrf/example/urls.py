"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import HelloAPI, booksAPI , bookAPI, BooksAPIMixins, BookAPIMixins, BookViewSet

router = routers.SimpleRouter()
router.register('books', BookViewSet)

urlpatterns = [
    #path('hello/', HelloAPI), #FBV
    path('hello/', HelloAPI.as_view()),
    #path('fbv/books/',booksAPI), cbv는 as_view로 참조
    path('fbv/books/',booksAPI.as_view()),
    #path('fbv/book/<int:bid>/',bookAPI),
    path('fbv/book/<int:bid>/',bookAPI.as_view()),
    
    path('mixin/books/', BooksAPIMixins.as_view()),
    path('mixin/book/<int:bid>/', BookAPIMixins.as_view()),
]

urlpatterns = router.urls




