from django.urls import path
from . import views

urlpatterns = [
    path('base/', views.base, name='base'),
    path('', views.index, name='index'),
    path('join/', views.join, name='join'),
    path('personal_home/', views.personal_home, name='personal_home'),
]