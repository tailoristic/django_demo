from django.urls import path, register_converter
from . import views
from . import converters

register_converter(converters.FourDigitYearConverter, 'yyyy')

urlpatterns = [
    path('dynamicUrl/', views.home_page, name='dynamicHome'),
    # path('dynamicUrl/<int:my_id>/', views.show_details, name="dynamicUrl"),
    path('dynamicUrl/<int:my_id>/<int:my_subid>/', views.show_subdetails, name="subdynamicUrl"),
    path('dynamicUrl/<yyyy:year>/',views.custom_path)
]
