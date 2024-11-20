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
from django.urls import path
from config.views import main, burger_list,burger_search,burger_create

urlpatterns = [
    path('admin/', admin.site.urls), #http://127.0.0.1:8000/admin/
    path("", main), #http://127.0.0.1:8000/
    path('burgers/',burger_list), #http://127.0.0.1:8000/burgers/
    path('search/', burger_search),
]
