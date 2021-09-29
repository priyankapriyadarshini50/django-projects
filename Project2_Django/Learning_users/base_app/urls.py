from django.urls import path
from base_app import views

# Template tagging
app_name = 'base_app'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    # path('special/', views.special, name='special'),
    # path('logout/', views.user_logout, name='logout'),
]
