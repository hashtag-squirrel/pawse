from django.urls import path
from cats.views import CatsView

urlpatterns = [
    path('', CatsView.as_view(), name='cats'),
]
