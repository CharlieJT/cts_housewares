from django.test import TestCase
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth.models import User


class Testtome_Cusr_Registration_Form(TestCase):

    def test_a_valid_registration_all_required_fields(self):
        registration_form = UserRegistrationForm({'email': 'test@gmail.com',
                                         'username': 'test',
                                         'password1': 'askdjhklhjasd123',
                                         'password2': 'askdjhklhjasd123',
                                         'first_name': 'test first name',
                                         'last_name': 'test last name'})

        self.assertTrue(registration_form.is_valid())

    def test_an_invalid_registration_if_email_field_is_empty(self):
        registration_form = UserRegistrationForm({'email': '',
                                         'username': 'test',
                                         'password1': 'askdjhklhjasd123',
                                         'password2': 'askdjhklhjasd123',
                                         'first_name': 'test first name',
                                         'last_name': 'test last name'})

        self.assertFalse(registration_form.is_valid())

    def test_an_invalid_registration_if_username_field_is_empty(self):
        registration_form = UserRegistrationForm({'email': 'test@gmail.com',
                                         'username': '',
                                         'password1': 'askdjhklhjasd123',
                                         'password2': 'askdjhklhjasd123',
                                         'first_name': 'test first name',
                                         'last_name': 'test last name'})

        self.assertFalse(registration_form.is_valid())

    def test_an_invalid_registration_if_password_1_field_is_empty(self):
        registration_form = UserRegistrationForm({'email': 'test@gmail.com',
                                         'username': 'test',
                                         'password1': '',
                                         'password2': 'askdjhklhjasd123',
                                         'first_name': 'test first name',
                                         'last_name': 'test last name'})

        self.assertFalse(registration_form.is_valid())

    def test_an_invalid_registration_if_password_2_field_is_empty(self):
        registration_form = UserRegistrationForm({'email': 'test@gmail.com',
                                         'username': 'test',
                                         'password1': 'askdjhklhjasd123',
                                         'password2': '',
                                         'first_name': 'test first name',
                                         'last_name': 'test last name'})

        self.assertFalse(registration_form.is_valid())

    def test_an_invalid_registration_if_password_1_field_does_not_match_password_2(self):
        registration_form = UserRegistrationForm({'email': 'test@gmail.com',
                                         'username': 'test',
                                         'password1': 'askdjhklhjasd123',
                                         'password2': 'we563dfhr76y8ri6jd',
                                         'first_name': 'test first name',
                                         'last_name': 'test last name'})

        self.assertFalse(registration_form.is_valid())

    def test_an_invalid_registration_if_first_name_field_is_empty(self):
        registration_form = UserRegistrationForm({'email': 'test@gmail.com',
                                         'username': 'test',
                                         'password1': 'askdjhklhjasd123',
                                         'password2': 'askdjhklhjasd123',
                                         'first_name': '',
                                         'last_name': 'test last name'})

        self.assertFalse(registration_form.is_valid())

    def test_an_invalid_registration_if_last_name_field_is_empty(self):
        registration_form = UserRegistrationForm({'email': 'test@gmail.com',
                                         'username': 'test',
                                         'password1': 'askdjhklhjasd123',
                                         'password2': 'askdjhklhjasd123',
                                         'first_name': 'test first name',
                                         'last_name': ''})

        self.assertFalse(registration_form.is_valid())

    

    
