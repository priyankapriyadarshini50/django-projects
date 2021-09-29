from django import forms
from AppTwo.models import UsersInformation


class UserNewForm(forms.ModelForm):
    class Meta:
        model = UsersInformation
        fields = '__all__'
