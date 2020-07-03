from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "shop/index.htm")

def about(request):
    return HttpResponse("I am about Page")

def contact(request):
    return HttpResponse("I am contact Page")

def tracker(request):
    return HttpResponse("I am tracker Page")

def search(request):
    return HttpResponse("I am search Page")

def productView(request):
    return HttpResponse("I am Product Page")

def checkout(request):
    return HttpResponse("I am checkout Page")
