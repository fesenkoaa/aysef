from django.urls import path
from .views import MainPage

urlpatterns = [
    path('main/', MainPage.as_view(), name='main'),
]

