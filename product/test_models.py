from django.test import TestCase
from .models import Product, Specification

# Create your tests here.
class TestViews(TestCase):

    def test_create_product(self):
        product = Product(
            item_number = "T900014",
            description = "Ice Diamond 28cm Frying Pan Ice Grey",
            brand = "Ice Diamond",
            about_product = "Made from heavy gauge, heat-resistant forget aluminium and coated with a superior diamond non-stick inner coating, this 28cm frying pan is ideal for preparing healthy, low-oil meals for the whole family. With a sturdy riveted steel handle and bonded steel base, this pan is suitable for all hobs, while its unique, ice textured exterior creates a unique visual feature for your kitchen. It's oven-safe up to 280 degrees and dishwasher safe, making it as easy to clean.",
            price = 16.66,
            stock = 74,
            item_height = 5.00,
            item_length = 29.10,
            item_width = 49.60,
            package_height = 7.20,
            package_length = 28.00,
            package_width = 49.50,
        )

        specification = Specification(
            specification = "Superior diamond reinforced non-stick interior."
        )
        product.save()
        self.assertEqual(product.item_number, "T900014")
        self.assertEqual(product.description, "Ice Diamond 28cm Frying Pan Ice Grey")
        self.assertEqual(product.price, 16.66)
        self.assertEqual(product.item_width, 49.60)
        self.assertEqual(specification.specification, "Superior diamond reinforced non-stick interior.")