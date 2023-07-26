from django.shortcuts import render
from django.views import generic, View
from django.http import HttpResponse


class Home(View):

    def get(self, request):
        template_name = 'index.html'
        return render(request, template_name)
