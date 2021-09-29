from django import forms
from django.core import validators


# custom validator for name form field
def start_with_z(value):
    if value.lower().startswith != 'z':
        raise forms.ValidationError('Please enter a name which start with z')


class FormName(forms.Form):
    name = forms.CharField(validators=[start_with_z])
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    # we can use a built-in validators
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput,
                                 validators=[validators.MaxLengthValidator(0)])

    # custom validator using default method clean_fieldName
    # def clean_botcatcher(self):
        #print("I am inside the botcatcher clean method")
        #botcatcher = self.cleaned_data.get('botcatcher')
        #print(botcatcher)
        #print(len(botcatcher))
        #if len(botcatcher) > 0:
            #raise forms.ValidationError("got a botcatcher")
        #return botcatcher




