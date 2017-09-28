from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('landing/index.html')
    context = {}
    return HttpResponse(template.render(context, request))
    # return HttpResponse("Hello, world. You're at the polls index.")