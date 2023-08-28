from django.test import TestCase


# Create your tests here.
class TestPagesViews(TestCase):

    def test_get_home_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')