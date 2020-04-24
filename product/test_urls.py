from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import all_products, product

# Create your tests here.
class TestUrls(SimpleTestCase):

    def test_product_url_is_resolved(self):
        url = reverse('all_products')
        self.assertEqual(resolve(url).func, all_products)