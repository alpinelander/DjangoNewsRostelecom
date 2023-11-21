from django.shortcuts import render
#from django.http import HttpResponse
# Create your views here.
from .models import News, Product
def index(request):
    water = Product('Боржоми вода', 40, 2)
    chokolate = Product('Шоколоад', 85, 1)
    colors = ['red','blue','golden','black']
    l = ['раз', 'два', 'три']
    value = 10
    context = {'title':'Главная страница',
               'Header1': 'Заголовок из шаблона',
               'value' : value,
               'numbers' : l,
               'colors' : colors,
               'water': water,
               'chokolate': chokolate,
               }
    return render(request,'main/index.html', context)
def about(request):
    return render(request,'main/about.html')
def contacts(request):
    return render(request,'main/contacts.html')
def content(request):
    return render(request,'main/content.html')
def sitebar(request):
    return render(request,'main/sitebar.html')
def create_user(request):
    return render(request,'main/create.html')
def profile(request):
    return render(request,'main/profile.html')
def signin(request):
    return render(request,'main/signin.html')
def news(request):
    return render(request,'main/news.html')
