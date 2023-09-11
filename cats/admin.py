from django.contrib import admin
from .models import Cat, CatApplication

# Register your models here.


@admin.register(Cat)
class CatAdmin(admin.ModelAdmin):
    """
    Register the Cat Model in the Admin area
    """
    list_display = (
        'pk',
        'name',
        'date_of_birth',
        'slug',
        'description',
        'image',
        )


@admin.register(CatApplication)
class CatApplicationAdmin(admin.ModelAdmin):
    """
    Register the CatApplication Model in the Admin area
    """
    list_display = ('pk', 'user', 'cat', 'application_text',)
