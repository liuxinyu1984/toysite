from django.urls import path
from . import views

urlpatterns = [
    path('', views.ManageMyCourseListView.as_view(), name='my_classes'),
    path('<int:course_id>/summary', views.course_summary, name='course_summary'),
]
