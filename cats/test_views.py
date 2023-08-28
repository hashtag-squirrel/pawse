from django.test import TestCase
from django.urls import reverse_lazy
from .models import Cat, User, CatApplication
from datetime import date


# Create your tests here.
class TestCatsViews(TestCase):

    def setUp(self):
        # Initialize and login a test user
        self.username = 'testuser'
        self.email = 'test@test.com'
        self.password = '12345'
        self.user = User(username=self.username, email=self.email)
        self.user.set_password(self.password)
        self.user.save()
        login = self.client.login(username=self.username, password=self.password)
        self.assertEqual(login, True)

    def test_cats_view(self):
        # Tests the basic cats view
        response = self.client.get('/cats/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cats.html')

    def test_application_view(self):
        # Tests the cat application view
        cat = Cat.objects.create(
            name='Cat',
            date_of_birth=date.today(),
            slug='cat',
            description='Test Description',
            image='url',
            )
        response = self.client.post(
            f'/cats/application/{cat.slug}',
            {
                'application_text': 'Test Text',
                'user': self.user,
                'cat': cat
            }
            )
        
        # Tests that the user gets redirected to the cats page
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/cats/')

        # Tests that the application was created successfully
        self.assertEqual(CatApplication.objects.last().application_text, 'Test Text')

    def test_application_edit_view(self):
        # Tests the cat application edit view
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
        response = self.client.put(
            f'/cats/application/{application.pk}/edit',
            {
                'application_text': 'New Test Text'
            }
            )

        application.refresh_from_db()
        updated_application = CatApplication.objects.get(pk=1)

        print(updated_application.application_text)

        # Tests successful submission
        self.assertEqual(response.status_code, 200)

        # Tests that the application text was updated
        self.assertEqual(updated_application.application_text, 'New Test Text')
