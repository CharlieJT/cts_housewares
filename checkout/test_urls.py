from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import checkout, successful_payment

# Create your tests here.
class TestUrls(SimpleTestCase):

    def test_checkout_url_is_resolved(self):
        url = reverse('checkout')
        self.assertEqual(resolve(url).func, checkout)

    def test_successful_payment_url_is_resolved(self):
        url = reverse('successful_payment')
        self.assertEqual(resolve(url).func, successful_payment)