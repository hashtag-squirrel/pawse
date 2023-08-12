from django.urls import path
from cats.views import CatsView, CatApplicationView

urlpatterns = [
    path('', CatsView.as_view(), name='cats'),
    path('application/<slug:slug>', CatApplicationView.as_view(),
         name='cat-application'),
]
