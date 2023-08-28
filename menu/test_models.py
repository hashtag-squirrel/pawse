from django.test import TestCase
from .models import MenuCategory, MenuItem


# Create your tests here.
class TestMenuModels(TestCase):

    def test_category_string_method_returns_name(self):
        category = MenuCategory.objects.create(name='Test Category', order=1)
        self.assertEqual(str(category), 'Test Category')

    def test_menuitem_string_method_returns_name(self):
        category = MenuCategory.objects.create(name='Test Category', order=1)
        menu_item = MenuItem.objects.create(
            name='Test Item',
            category=category,
            price=1.00
            )
        self.assertEqual(str(menu_item), 'Test Item')
