from django.db import models


class Cat(models.Model):

    name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    description = models.TextField()
    image = models.ImageField()

    class Meta:
        ordering = ['-name']

    def __str__(self):
        return self.name
