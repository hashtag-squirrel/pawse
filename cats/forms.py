from .models import CatApplication, Cat
from django import forms


class CatInterestForm(forms.ModelForm):

    class Meta:
        model = CatApplication
        fields = ('application_text',)
