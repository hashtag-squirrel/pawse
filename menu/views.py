from django.shortcuts import render
from django.views import generic, View
from menu.models import MenuCategory, MenuItem


class MenuView(generic.ListView):

    model = MenuCategory
    queryset = MenuCategory.objects.all()
    template_name = 'menu.html'
