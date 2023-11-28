"""
URL configuration for NewsStudyRostelecom project.

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
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('product/<int:a>/details',views.get_demo),
    path('calc/<int:a>/<slug:operation>/<int:b>',views.calc),
    path('about/', views.about, name='o saite'),
    path('contacts/', views.contacts, name='telefon'),
    path('content/', views.content, name='content'),
    path('create/', views.create_user, name='create'),
#    path('news/', views.news, name='news'),
    path('profile/', views.profile, name='profile'),
    path('signin/', views.signin, name='signin'),
    path('sitebar/', views.sitebar, name='sitebar'),
    path('header/', views.header, name='header'),
    path('body/', views.body, name='body'),
    path('last_news/', views.last_news, name='last_news'),
]
