from django.shortcuts import render
from django.views import View


class Home(View):
    """
    Displays the index.html template
    """

    def get(self, request):
        template_name = 'index.html'
        return render(request, template_name)
