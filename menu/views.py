from typing import Any, Dict
from django.shortcuts import render
from django.views import generic, View
from menu.models import MenuCategory, MenuItem


class MenuView(generic.ListView):

    model = MenuCategory
    categories = MenuCategory.objects.all()
    template_name = 'menu.html'

    def get_context_data(self, **kwargs: Any):
        context = super(MenuView, self).get_context_data(**kwargs)
        context['menu_items'] = MenuItem.objects.all()
        return context
