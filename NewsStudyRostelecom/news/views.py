from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import *
# Create your views here.
def news(request):
    return render(request,'news/news.html')

def index(request):
    article = Article.objects.all().first()
    context = {'article':article}
    return render(request,'news/index.html',context)

def detail(request,id):
    article = Article.objects.filter(id=id).first()
    return HttpResponse(f'<h1>{ article.title }</h1>')
