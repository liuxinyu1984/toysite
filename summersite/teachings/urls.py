from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_classes, name='my_classes'),
]
