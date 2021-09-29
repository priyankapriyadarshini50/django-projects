from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import SchoolInfo
import requests


# Create your views here.
class IndexView(TemplateView):
    template_name = 'school_basic/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['insert_me'] = 'Hi, inserted from the TemplateView'
        return context


class SchoolInfoListView(ListView):
    model = SchoolInfo







