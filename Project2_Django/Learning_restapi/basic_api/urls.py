from django.urls import path
from basic_api import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('generic/', views.ArticleGenericView.as_view(), name='genericview'),
    path('detail/<int:pk>/', views.ArticleDetailView.as_view(), name='detailview'),
    path('article/', views.article_list, name='article_list'),
    path('article/<int:pk>/', views.article_details, name='article_detail'),
    path('article/api', views.article_apiview_list, name='article_apiview_list'),
    path('article/api/<int:pk>/', views.article_apiview_detail, name='article_apiview_detail'),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
