from django.urls import path,include
from formApp import views
urlpatterns = [
    path('registration/',views.formRendering),
    path('form-attrib/',views.formAttrib),
    path('success/',views.thanks),
    path('form-inputs/',views.formInputs)
]
