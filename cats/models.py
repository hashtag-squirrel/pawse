from django.db import models
import datetime
from django.contrib.auth.models import User
from autoslug import AutoSlugField


class Cat(models.Model):
    """
    Cat Model
    contains all information about each cat, including an image
    """

    name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    slug = AutoSlugField(populate_from='name', unique_with='date_of_birth')
    description = models.TextField()
    image = models.ImageField()
    applications = models.ManyToManyField(
        User,
        through='CatApplication',
        blank=True)

    class Meta:
        ordering = ['-name']

    def __str__(self):
        return self.name

    def get_age(self):
        """
        Method which calculates the age from date of birth
        """
        age = datetime.date.today()-self.date_of_birth

        number_of_days = int((age).days)

        # Calculating years
        years = number_of_days // 365

        # Calculating months
        months = (number_of_days - years * 365) // 30

        # Calculating days
        days = (number_of_days - years * 365 - months*30)

        return f'{years} years, {months} months and {days} days old'

    def number_of_applications(self):
        """
        Returns the number of applications for a cat
        """
        return self.applications.count()


class CatApplication(models.Model):
    """
    CatApplication Model
    used as a helper model for the ManyToMany Relationship from Cat to User
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)
    application_text = models.TextField()

    def __str__(self):
        return f'You have sent an application for {self.cat}.'
