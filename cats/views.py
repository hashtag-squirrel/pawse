from django.shortcuts import render, get_object_or_404, reverse  # noqa
from django.views import generic
from .models import Cat, CatApplication
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class CatsView(generic.ListView):

    model = Cat
    context_object_name = 'cats'
    template_name = 'cats.html'

    def get_context_data(self, **kwargs):
        context = super(CatsView, self).get_context_data(**kwargs)
        context['applications'] = CatApplication.objects.filter(
            user=self.request.user.id)
        return context

    # def get(self, request, *args, **kwargs):
    #     queryset = Cat.objects.all()
    #     cat = get_object_or_404(queryset)
    #     applied = False

    #     if cat.applications.filter(user=self.request.user.id).exists():
    #         applied = True

    #     return render(
    #         request,
    #         'cats.html',
    #         {
    #             "applied": applied,
    #         },
    #     )


@method_decorator(login_required, name='dispatch')
class CatApplicationView(generic.CreateView):

    model = CatApplication

    fields = ['application_text']

    template_name = 'cat-application.html'

    def get_success_url(self):
        return reverse('cats')
    
    def get_context_data(self, **kwargs):
        context = super(CatApplicationView, self).get_context_data(**kwargs)
        context['slug'] = self.kwargs['slug']
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.cat = Cat.objects.get(slug=self.kwargs['slug'])
        return super(CatApplicationView, self).form_valid(form)
