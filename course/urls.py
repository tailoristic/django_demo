from django.urls import path
from . import views

# INDEPENDENT URL PATTERNS
urlpatterns = [
    path('course/', views.my_fun),
    path('dynamic/',views.dashboard)
]
