from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil

# Create your views here.


def index(request):
    # products = Product.objects.all()
    # print(products)
    # n = len(products)
    # nSlide = n//4 + ceil((n/4)-(n//4))
    # params = {'no_of_slides':nSlide, 'range':range(1,nSlide),   'product': products}
    # allProds = [[products,range(1,nSlide),nSlide],
    #             [products,range(1,nSlide),nSlide]]
    allProds = []
    catprods = Product.objects.values('category','id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlide = n//4 + ceil((n/4)-(n//4))
        allProds.append([prod,range(1,nSlide),nSlide])
    params = {'allProds':allProds}
    return render(request, 'shop/index.html', params)

def about(request):
    return render(request,'shop/about.html')

def contact(request):
    return HttpResponse("We are at contact")

def tracker(request):
    return HttpResponse("We are at tracker")

def search(request):
    return HttpResponse("We are at search")

def productView(request):
    return HttpResponse("We are at product view")

def checkout(request):
    return HttpResponse("We are at checkout")
