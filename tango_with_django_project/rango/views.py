from django.http import HttpResponse
from django.core.urlresolvers import reverse

def index(request):
    return HttpResponse("Hello world? <a href='/rango/about'>About</a>")

def about(request):
    return HttpResponse("This is About page. <a href='/rango'>Index</a>")