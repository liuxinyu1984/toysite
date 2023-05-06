from typing import Any, Dict, Optional
from django.db import models
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from courses.models import Course, Lecture, UploadNote, UploadVideo
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import CreateLectureForm, CreateNoteForm, CreateVideoForm
from django.urls import reverse_lazy


# @login_required(login_url="/users/login/")
# def my_classes(request):
#     my_courses = Course.objects.filter(
#         instructor=request.user).order_by('subject', 'course_number')
#     return render(
#         request,
#         'my_classes.html',
#         {
#             'my_courses': my_courses,
#             'user': request.user,
#         }
#     )


# def course_summary(request, course_id):
#     this_course = get_object_or_404(Course, pk=course_id)
#     lectures = Lecture.objects.filter(
#         course=this_course).order_by('week', 'created_at')
#     return render(
#         request,
#         'single_class.html',
#         {
#             'course': this_course,
#             'lectures': lectures,
#         }
#     )


class ViewMyCourses(ListView):
    model = Course
    template_name = 'my_courses.html'

    def get_queryset(self) -> QuerySet[Any]:
        qs = super(ViewMyCourses, self).get_queryset()
        return qs.filter(instructor=self.request.user)


class CourseDetail(DetailView):
    model = Course
    template_name = 'course_detail.html'
    pk_url_kwarg = 'course_id'

    # def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
    #     return super().get_context_data(**kwargs)


class LectureDetail(DetailView):
    model = Lecture
    template_name = 'lecture_detail.html'
    pk_url_kwarg = 'lecture_id'

    # def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
    #     context = super(LectureDetail, self).get_context_data(**kwargs)


class CreateLectureView(CreateView):
    model = Lecture
    template_name = 'create_lecture.html'
    # fields = '__all__'
    form_class = CreateLectureForm

    def get_initial(self):
        return {'course': Course.objects.get(id=self.kwargs['course_id'])}

    # def form_valid(self, form):
    #     print(self.request)
    #     lecture = form.save(commit=False)
    #     lecture.course = Course.objects.all().filter(
    #         pk=self.kwargs['course_id'])
    #     return super(CreateLectureView, self).form_valid(form)


class UpdateLectureView(UpdateView):
    model = Lecture
    template_name = 'update_lecture.html'
    fields = ['title', 'week', 'syllabus', 'is_midterm', 'is_final']


class DeleteLectureView(DeleteView):
    model = Lecture
    template_name = 'delete_lecture.html'

    def get_success_url(self) -> str:
        return reverse_lazy('course_detail', kwargs={
            'course_id': self.object.course.id})


class CreateNoteView(CreateView):
    model = UploadNote
    template_name = 'create_document.html'
    form_class = CreateNoteForm

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["lecture_id"] = self.kwargs['lecture_id']
        return context

    def get_initial(self):
        return {'lecture': Lecture.objects.get(id=self.kwargs['lecture_id'])}


class UpdateNoteView(UpdateView):
    model = UploadNote
    template_name = 'update_document.html'
    fields = ['title', 'document']


class DeleteNoteView(DeleteView):
    model = UploadNote
    template_name = 'delete_document.html'

    def get_success_url(self) -> str:
        return reverse_lazy('lecture_detail', kwargs={
            'course_id': self.object.lecture.course.id,
            'lecture_id': self.object.lecture.id
        })


class CreateVideoView(CreateView):
    model = UploadVideo
    template_name = 'create_video.html'
    form_class = CreateVideoForm

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["lecture_id"] = self.kwargs['lecture_id']
        return context

    def get_initial(self):
        return {'lecture': Lecture.objects.get(id=self.kwargs['lecture_id'])}
