from django.test import TestCase
from .models import Cat, CatApplication, User
from datetime import date, timedelta, datetime


# Create your tests here
class TestCatModels(TestCase):

    def setUp(self):
        # Initialize and login a test user
        self.username = 'testuser'
        self.email = 'test@test.com'
        self.password = '12345'
        self.user = User(username=self.username, email=self.email)
        self.user.set_password(self.password)
        self.user.save()
        login = self.client.login(
            username=self.username,
            password=self.password
            )
        self.assertEqual(login, True)

    def test_cat_string_method_returns_name(self):
        cat = Cat.objects.create(
            name='Cat',
            date_of_birth=date.today(),
            slug='cat',
            description='Test Description',
            image='url',
            )
        self.assertEqual(str(cat), 'Cat')

    def test_number_of_applications(self):
        cat = Cat.objects.create(
            name='Cat',
            date_of_birth=date.today(),
            slug='cat',
            description='Test Description',
            image='url',
            )
        CatApplication.objects.create(
            user=self.user,
            cat=cat,
            application_text='Test Text'
            )
        number = cat.number_of_applications()
        self.assertEqual(number, 1)

    def test_get_age(self):
        cat = Cat.objects.create(
            name='Cat',
            date_of_birth=(date.today() - timedelta(days=1)),
            slug='cat',
            description='Test Description',
            image='url',
            )
        self.assertEqual(cat.get_age(), '0 years, 0 months and 1 days old')

    def test_cat_application_string_method_returns_application_details(self):

        cat = Cat.objects.create(
            name='Cat',
            date_of_birth=date.today(),
            slug='cat',
            description='Test Description',
            image='url',
            )
        application = CatApplication.objects.create(
            user=self.user,
            cat=cat,
            application_text='Test Text'
            )
        self.assertEqual(
            str(application),
            'You have sent an application for Cat. It says: "Test Text"'
            )
