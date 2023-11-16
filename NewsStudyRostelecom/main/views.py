from django.shortcuts import render
#from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'main/index.html')
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
