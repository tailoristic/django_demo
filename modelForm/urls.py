from django.urls import path,include
from modelForm import views
urlpatterns = [
    path('model-form/',views.modelForm)
]
