from django import forms
from django.contrib.auth.models import User
from base_app.models import UserProfileInfo
from django.core import validators


# below class takes the user input for django built-in User model
class UserForm(forms.ModelForm):
    # for custom validation we need to provide the field explicitly
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        # the following fields will display on the webpage
        fields = ('username', 'password', 'email')


# custom validator for portfolio_link
def contain_https(value):
    if not (value.startswith('https')):
        raise forms.ValidationError("Please enter a link with https://")


# created a UserProfileInfoForm for user to provide portfolio_link and profile_pic
class UserProfileInfoForm(forms.ModelForm):
    portfolio_link = forms.URLField(required=False, validators=[contain_https])

    class Meta:
        model = UserProfileInfo
        fields = ('portfolio_link', 'profile_pic')
