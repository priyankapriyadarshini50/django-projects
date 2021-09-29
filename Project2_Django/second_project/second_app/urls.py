from django.urls import path
from second_app import views

urlpatterns = [
    path('users/', views.user_info, name='users'),
    path('signup/', views.signup, name='signup'),
]
