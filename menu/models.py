from django.db import models

# Create your models here.


class MenuCategory(models.Model):
    """
    MenuCategory Model
    used to categorize MenuItems
    Sorted by the 'order' field
    """

    name = models.CharField(max_length=30, unique=True)
    order = models.IntegerField(unique=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    """
    MenuItem Model
    """

    name = models.CharField(max_length=50)
    category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE,
                                 related_name='category')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['-name']

    def __str__(self):
        return self.name
