from django.urls import path,include
from . import views
urlpatterns = [
    path('query/',views.home_index)
]
