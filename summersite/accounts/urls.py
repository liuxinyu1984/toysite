from django.urls import path
from . import views


urlpatterns = [
    path('', views.base, name="base"),
    path('home/', views.home_page, name="homepage"),
    path('join/', views.join, name="join"),
]