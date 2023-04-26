from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from courses.models import Course, Lecture, UploadNote, UploadVideo


@login_required(login_url="/users/login/")
def my_classes(request):
    my_courses = Course.objects.filter(
        instructor=request.user).order_by('subject', 'course_number')
    return render(
        request,
        'my_classes.html',
        {
            'my_courses': my_courses,
            'user': request.user,
        }
    )


def course_summary(request, course_id):
    this_course = get_object_or_404(Course, pk=course_id)
    lectures = Lecture.objects.filter(
        course=this_course).order_by('week', 'created_at')
    return render(
        request,
        'single_class.html',
        {
            'course': this_course,
            'lectures': lectures,
        }
    )
