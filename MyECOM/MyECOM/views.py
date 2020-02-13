# from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<center><h1> Hi I am an index of main project </h1></center>")