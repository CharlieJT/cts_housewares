from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import logout, login, registration, user_profile

# Create your tests here.
class TestUrls(SimpleTestCase):

    def test_logout_url_is_resolved(self):
        url = reverse('logout')
        self.assertEqual(resolve(url).func, logout)

    def test_login_url_is_resolved(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func, login)

    def test_registration_url_is_resolved(self):
        url = reverse('registration')
        self.assertEqual(resolve(url).func, registration)

    def test_user_profile_url_is_resolved(self):
        url = reverse('profile')
        self.assertEqual(resolve(url).func, user_profile)