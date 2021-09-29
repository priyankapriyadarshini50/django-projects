from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('form/', views.form_name_view, name='form'),
    path('image/', views.image_view, name='image'),
    ]
