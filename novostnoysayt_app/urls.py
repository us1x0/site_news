from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page),
    path('news/', views.news_today),
    path('contacts/', views.contacts)
]