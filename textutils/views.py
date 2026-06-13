from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'index.html')
    # return HttpResponse("Home Page")

def about(request):
    return HttpResponse("About Page")

def removepunc(request):
    return HttpResponse('Remove Punc')

def spaceremove(request):
    return HttpResponse("Remove Space  <a href='/'> back </a>")

def capitalizefirst(request):
    return HttpResponse("capitaal The letter")

def charcount(request):
    return HttpResponse("count The letter ")


