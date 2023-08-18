from django.contrib import admin
from .models import Cat, CatApplication

# Register your models here.


@admin.register(Cat)
class CatAdmin(admin.ModelAdmin):
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
    list_display = ('pk', 'user', 'cat', 'application_text',)
