from django.template import RequestContext
from django.shortcuts import render_to_response
from rango.models import Category
from rango.models import Page

def index(request):
    context = RequestContext(request)

    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}

    return render_to_response('rango/index.html', context_dict, context)

def category(request, category_name_url):
    context = RequestContext(request)

    category_name = category_name_url.replace('_', ' ')
    context_dict = {'category_name': category_name}

    try:
        category = Category.objects.get(name=category_name)


def about(request):
    context = RequestContext(request, {'welcomemessage': 'Welcome!'})
    return render_to_response('rango/about.html', context)
