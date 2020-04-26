from django.test import TestCase
from django.contrib.auth.models import User
from .models import Order, OrderLineItem

# Create your tests here.
class TestViews(TestCase):

    def setUp(self):

        # Create Password
        password = 'password123' 

        # Create Super User
        my_admin = User.objects.create_superuser('test_user', 'test_email@test.com', password)

        # Log user in
        logged_in = self.client.login(username=my_admin.username, password=password)


    def test_create_order(self):
        
        # Create an order
        order = Order(
            first_name = "User",
            last_name = "Name",
            address_line_1 = "1 Example Close",
            address_line_2 ="Area",
            address_line_3 = "County",
            town_or_city = "Town",
            postcode = "EX4M 9LE",
            country = "Country",
            phone_number = "07123456789",
        )

        # Create an order line item
        order_line_item = OrderLineItem(
            price = 11.99,
            quantity = 7
        )

        self.assertEqual(order.first_name, "User")
        self.assertEqual(order.address_line_1, "1 Example Close")
        self.assertEqual(order.town_or_city, "Town")
        self.assertEqual(order.postcode, "EX4M 9LE")
        self.assertEqual(order_line_item.price * order_line_item.quantity, 83.93)