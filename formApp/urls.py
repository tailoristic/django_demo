from django.urls import path,include
from formApp import views
urlpatterns = [
    path('registration/',views.formRendering)
]
