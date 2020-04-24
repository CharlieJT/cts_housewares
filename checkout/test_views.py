from django.test import TestCase

# Create your tests here.
class TestViews(TestCase):

    def test_checkout_page(self):
        page = self.client.get("/checkout/")
        self.assertEqual(page.status_code, 302)

    def test_successful_payment_page(self):
        page = self.client.get("/checkout/successful_payment")
        self.assertEqual(page.status_code, 301)
    