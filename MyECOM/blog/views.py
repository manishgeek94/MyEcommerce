from django.shortcuts import render
from dataclasses import dataclass

# Create your views here.


from django.http import HttpResponse

# Create your views here.

def index(request):
    return  render(request,'blog/index.html')


