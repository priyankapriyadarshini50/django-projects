from django.urls import path
from AppTwo import views

urlpatterns = [
    path('', views.home, name='home'),
    path('users/', views.usersInfo, name='usersInfo'),
    path('signup/', views.user_signup, name='signup'),
    path('thankyou/', views.thankYou, name='thankyou')
]
