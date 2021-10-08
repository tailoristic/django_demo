from . import views
from django.urls import path

urlpatterns = [
    path('signup/', views.sign_up, name="auth-sign"),
    path('login/', views.user_login, name="auth-login"),
    path('profile/', views.user_profile, name="profile"),
    path('logout/', views.user_logout, name="logout"),
    path('change-password/', views.changePassword, name="changePass"),
    path('change-password1/', views.changePassword1, name="changePass1"),
    path('userdetails/<int:id>', views.user_details, name="userdetails"),
]
