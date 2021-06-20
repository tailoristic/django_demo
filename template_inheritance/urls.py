from django.urls import path
from . import views
urlpatterns = [
    path('base/', views.master_index),
    path('home_page/', views.home_page),
    path('about-page/', views.about_page),
]