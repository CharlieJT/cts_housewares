from django.test import TestCase
from django.contrib.auth.models import User

# Create your tests here.
class TestViews(TestCase):

    def setUp(self):

        # Create Password
        password = 'password123' 

        # Create Super User
        my_admin = User.objects.create_superuser('test_user', 'test_email@test.com', password)

        # Log user in
        logged_in = self.client.login(username=my_admin.username, password=password)


    def test_checkout_page(self):
        page = self.client.get("/checkout/")
        self.assertEqual(page.status_code, 200)

    def test_successful_payment_page(self):
        page = self.client.get("/checkout/successful_payment")
        self.assertEqual(page.status_code, 301)
    