from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Cat, CatApplication
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class CatsView(generic.ListView):

    model = Cat
    context_object_name = 'cats'
    template_name = 'cats.html'


@method_decorator(login_required, name='dispatch')
class CatApplication(generic.CreateView):

    model = CatApplication

    fields = ['application_text']

    template_name = 'cat-application.html'
