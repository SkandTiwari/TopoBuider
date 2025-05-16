from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member


def landing_page(request):
    # mymembers = Member.objects.all().values()
    template = loader.get_template('node_analyser_landing.html')
    # context = {
    #     'mymembers': mymembers,
    # }
    return HttpResponse(template.render())

def auth(request):
    template = loader.get_template('auth.html')
    return HttpResponse(template.render())