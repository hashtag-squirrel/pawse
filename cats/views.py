from django.shortcuts import reverse, HttpResponseRedirect
from django.views import generic
from .models import Cat, CatApplication
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages


class CatsView(generic.ListView):
    """
    Displays all objects of the Cat Model
    Displays all cat applications the specific user has
    """

    model = Cat
    context_object_name = 'cats'
    template_name = 'cats.html'

    def get_context_data(self, **kwargs):
        context = super(CatsView, self).get_context_data(**kwargs)
        context['applications'] = CatApplication.objects.filter(
            user=self.request.user.id)
        return context


@method_decorator(login_required, name='dispatch')
class CatApplicationView(generic.CreateView):
    """
    Allows authenticated users to create and save a cat application
    validates whether the user already has an application for that cat
    Redirects the user to the Cats page
    """

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
        user_application = CatApplication.objects.filter(
            user=self.request.user, cat=form.instance.cat)
        if user_application.count() > 0:
            messages.error(
                self.request,
                f'You already have an application for {form.instance.cat}!'
                )
            return HttpResponseRedirect('/cats')
        messages.success(self.request, 'SUCCESS! Application added!')
        return super(CatApplicationView, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class CatApplicationEditView(generic.UpdateView):
    """
    Allows authenticated users to update and save a cat application
    Redirects the user to the Cats page
    """

    model = CatApplication
    context_object_name = 'application'
    fields = ['application_text']

    template_name = 'cat-application-edit.html'

    def get_success_url(self):
        return reverse('cats')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'SUCCESS! Application edited!')
        return super(CatApplicationEditView, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class CatApplicationDeleteView(generic.DeleteView):
    """
    Allows authenticated users to delete a cat application
    Redirects the user to the Cats page
    """

    model = CatApplication
    context_object_name = 'application'

    template_name = 'cat-application-delete.html'

    def get_success_url(self):
        messages.success(self.request, 'SUCCESS! Application deleted!')
        return reverse('cats')
