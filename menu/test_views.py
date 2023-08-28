from django.test import TestCase


# Create your tests here.
class TestMenuViews(TestCase):

    def test_menu_view(self):
        response = self.client.get('/menu/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'menu.html')
