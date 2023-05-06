from django.urls import path
from . import views

urlpatterns = [
    path('', views.ViewMyCourses.as_view(), name='my_teaching_courses'),
    # path('<int:course_id>/summary', views.course_summary, name='course_summary'),
    path('<int:course_id>/course_detail',
         views.CourseDetail.as_view(), name='course_detail'),
    path('<int:course_id>/<int:lecture_id>/lecture_detail',
         views.LectureDetail.as_view(), name='lecture_detail'),
    path('<int:course_id>/create_lecture/',
         views.CreateLectureView.as_view(), name='create_lecture'),
    path('update_lecture/<int:pk>',
         views.UpdateLectureView.as_view(), name='update_lecture')
]
