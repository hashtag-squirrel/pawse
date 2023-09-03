from django.urls import path
from cats.views import CatsView, CatApplicationView, CatApplicationEditView, CatApplicationDeleteView  # noqa

urlpatterns = [
    path('', CatsView.as_view(), name='cats'),
    path('application/<slug:slug>', CatApplicationView.as_view(),
         name='cat-application'),
    path('application/<pk>/edit', CatApplicationEditView.as_view(),
         name='edit-application'),
    path('application/<pk>/delete', CatApplicationDeleteView.as_view(),
         name='delete-application')
]
