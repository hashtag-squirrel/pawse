from django.contrib import admin
from .models import MenuItem, MenuCategory


# Register your models here.
@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    """
    Register the MenuItem Model in the Admin area
    """
    list_display = ('name', 'category', 'price', 'description',)


@admin.register(MenuCategory)
class MenuCategoryAdmin(admin.ModelAdmin):
    """
    Register the MenuCategory Model in the Admin area
    """
    list_display = ('name', 'order',)
