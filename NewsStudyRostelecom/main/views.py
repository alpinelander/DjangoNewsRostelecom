from django.shortcuts import render
#from django.http import HttpResponse
# Create your views here.
from .models import News, Product
def index(request):

    if request.method == 'POST':
        print('Получили пост-запрос')
        print(request.POST)
        title = request.POST.get('title')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        new_product = Product(title, float(price), int(quantity))
        print('Создан товар: ', new_product.title, ', Общая сумма: ', new_product.price*new_product.quantity )
    else:
        print('Получили гет-запрос')
        print(request.GET)

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
