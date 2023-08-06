from django.db import models
import datetime


class Cat(models.Model):

    name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    description = models.TextField()
    image = models.ImageField()

    class Meta:
        ordering = ['-name']

    def __str__(self):
        return self.name

    def get_age(self):
        """Calculates the age from date of birth"""
        age = datetime.date.today()-self.date_of_birth

        number_of_days = int((age).days)

        # Calculating years
        years = number_of_days // 365

        # Calculating months
        months = (number_of_days - years * 365) // 30

        # Calculating days
        days = (number_of_days - years * 365 - months*30)

        return f'{years} years, {months} months and {days} days old'
