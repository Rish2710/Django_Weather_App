# # weather/urls.py
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.weather_view, name='weather_view'),  # Form input for city
# ]
from django.urls import path
from .views import weather_view

urlpatterns = [
    path('', weather_view, name='weather_view'),  # Adjust as needed
]
