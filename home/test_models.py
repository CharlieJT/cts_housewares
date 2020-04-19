from django.test import TestCase
from .models import Banner

# Create your tests here.
class TestModels(TestCase):

    def test_home_page_banners(self):
        banner = Banner(brand="Smeg", link="smeg")
        banner.save()
        self.assertEqual(banner.brand, "Smeg")
        self.assertEqual(banner.link, "smeg")


    def test_banner_as_a_string(self):
        banner = Banner(brand="Smeg", link="smeg")
        self.assertEqual("Smeg", str(banner))