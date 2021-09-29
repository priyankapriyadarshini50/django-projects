from django.urls import path
from . import views

app_name = 'school_basic'
urlpatterns = [
    path('', views.SchoolInfoListView.as_view(), name='list'),
]
