from django.db import models

# Create your models here.


class MenuCategory(models.Model):

    name = models.CharField(max_length=30, unique=True)

    class Meta:
        ordering = ['-name']

    def __str__(self):
        return self.name


class MenuItem(models.Model):

    name = models.CharField(max_length=50)
    category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE,
                                 related_name='category')
    price = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        ordering = ['-name']

    def __str__(self):
        return self.name