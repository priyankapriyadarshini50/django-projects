from django.views.generic import CreateView
from . import forms
from django.urls import reverse_lazy


# Create your views here.
class SignUpCreateView(CreateView):
    form_class = forms.SignUpForm
    url_success = reverse_lazy('login')
    template_name = 'accounts/signup.html'

