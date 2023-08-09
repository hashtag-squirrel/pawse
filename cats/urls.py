from django.urls import path
from cats.views import CatsView, CatApplication

urlpatterns = [
    path('', CatsView.as_view(), name='cats'),
    path('application/', CatApplication.as_view(), name='cat-application'),
]
