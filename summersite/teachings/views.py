from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from courses.models import Course, Lecture, UploadNote, UploadVideo


@login_required(login_url="/users/login/")
def my_classes(request):
    my_courses = Course.objects.filter(instructor=request.user)
    return render(
        request,
        'my_classes.html',
        {
            'my_courses': my_courses,
            'user': request.user,
        }
    )
