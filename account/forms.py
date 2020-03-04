from django import forms


class UserLoginForm(forms.Form):
    """ Form used to log the user in """
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)