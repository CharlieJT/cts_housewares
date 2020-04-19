from django.test import TestCase

# Create your tests here.
class TestViews(TestCase):

    def test_products_page(self):
        page = self.client.get("/product/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "products.html")
    
    