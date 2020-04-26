from django.test import TestCase
from django.contrib.auth.models import User
from .forms import MakePaymentForm, OrderForm

# Create your tests here.
class TestViews(TestCase):

    def setUp(self):

        # Create Password
        password = 'password123' 

        # Create Super User
        my_admin = User.objects.create_superuser('test_user', 'test_email@test.com', password)

        # Log user in
        logged_in = self.client.login(username=my_admin.username, password=password)


    def test_order_form_is_valid(self):

        order_form = OrderForm(data={
            'first_name': "User",
            'last_name': "Name",
            'address_line_1': "1 Example Close",
            'address_line_2':"Area",
            'address_line_3': "County",
            'town_or_city': "Town",
            'postcode': "EX4M 9LE",
            'country': "Country",
            'phone_number': "07123456789",
        })

        self.assertTrue(order_form.is_valid())
        self.assertEqual(order_form.data['first_name'], "User")
        self.assertEqual(order_form.data['address_line_1'], "1 Example Close")
        self.assertEqual(order_form.data['town_or_city'], "Town")
        self.assertEqual(order_form.data['postcode'], "EX4M 9LE")


    def test_make_payment_form_is_valid(self):

        make_payment_form = MakePaymentForm(data={
            'credit_card_number': '4242424242424242',
            'cvv': '111',
            'expiry_month': '2',
            'expiry_year': '2021',
            'stripe_id': 'pk_test_nbWefqblVg8HnYsFmpcld8qj'
        })

        self.assertTrue(make_payment_form.is_valid())
        self.assertEqual(make_payment_form.data['credit_card_number'], "4242424242424242")
        self.assertEqual(make_payment_form.data['cvv'], "111")
        self.assertEqual(make_payment_form.data['expiry_month'], "2")
        self.assertEqual(make_payment_form.data['expiry_year'], "2021")
        self.assertEqual(make_payment_form.data['stripe_id'], "pk_test_nbWefqblVg8HnYsFmpcld8qj")

    
    def test_form_is_not_valid_if_first_name_field_is_empty(self):

        order_form = OrderForm(data={
            'first_name': "",
            'last_name': "Name",
            'address_line_1': "1 Example Close",
            'address_line_2':"Area",
            'address_line_3': "County",
            'town_or_city': "Town",
            'postcode': "EX4M 9LE",
            'country': "Country",
            'phone_number': "07123456789",
        })

        self.assertFalse(order_form.is_valid())


    def test_form_is_not_valid_if_postcode_field_is_empty(self):

        order_form = OrderForm(data={
            'first_name': "User",
            'last_name': "Name",
            'address_line_1': "1 Example Close",
            'address_line_2':"Area",
            'address_line_3': "County",
            'town_or_city': "Town",
            'postcode': "",
            'country': "Country",
            'phone_number': "07123456789",
        })

        self.assertFalse(order_form.is_valid())


    def test_form_is_not_valid_if_phone_number_field_is_empty(self):

        order_form = OrderForm(data={
            'first_name': "User",
            'last_name': "Name",
            'address_line_1': "1 Example Close",
            'address_line_2':"Area",
            'address_line_3': "County",
            'town_or_city': "Town",
            'postcode': "EX4M 9LE",
            'country': "Country",
            'phone_number': "",
        })

        self.assertFalse(order_form.is_valid())


    def test_form_is_valid_if_address_line_2_field_is_empty(self):

        order_form = OrderForm(data={
            'first_name': "User",
            'last_name': "Name",
            'address_line_1': "1 Example Close",
            'address_line_2':"",
            'address_line_3': "County",
            'town_or_city': "Town",
            'postcode': "EX4M 9LE",
            'country': "Country",
            'phone_number': "07123456789",
        })

        self.assertTrue(order_form.is_valid())