from django.shortcuts import render
from django.views import generic, View
from .models import Cat


class CatsView(generic.ListView):

    model = Cat
    cats = Cat.objects.all()
    template_name = 'cats.html'
