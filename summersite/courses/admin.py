from django.contrib import admin
from .models import Term, Course, Lecture, UploadNote, UploadVideo
from django.utils.timezone import datetime

# admin.site.register(Course)


class TermAdmin(admin.ModelAdmin):
    def term_title(self, obj):
        return obj.year + " " + obj.season.lower()
    list_display = ('term_title', 'year', 'season', 'start_date', 'end_date')


admin.site.register(Term, TermAdmin)


class CourseAdmin(admin.ModelAdmin):

    def course_title(self, obj):
        return obj.subject + " " + obj.course_number

    def is_active(self, obj):
        return datetime.today().date() >= obj.term.start_date and datetime.today().date() <= obj.term.end_date

    list_display = ('course_title', 'term', 'section',
                    'instructor', 'is_active')
    # fields = ['subject', 'course_number', 'term', 'section', 'instructor', 'start_date', 'end_date']
    fieldsets = (
        ('Course', {'fields': ('subject', 'course_number', 'section')}),
        ('Time', {'fields': ('term',)}),
        ('Instructor', {'fields': ('instructor',)})
    )
    ordering = ['subject', 'course_number', 'instructor']
    list_filter = ('subject', 'instructor')
    search_fields = ['subject', 'instructor__username']


admin.site.register(Course, CourseAdmin)


class LectureAdmin(admin.ModelAdmin):

    # def course_title(self):
    #     return self.course.__str__()

    list_display = ('course', 'week', 'created_at',
                    'updated_at', 'is_midterm', 'is_final')
    # prepopulated_fields = {"slug": ['course', 'week']}


admin.site.register(Lecture, LectureAdmin)


class UploadNoteAdmin(admin.ModelAdmin):
    list_display = (
        'lecture', 'title', 'upload_time'
    )


admin.site.register(UploadNote, UploadNoteAdmin)


class UploadVideoAdmin(admin.ModelAdmin):
    list_display = (
        'lecture', 'title', 'upload_time'
    )


admin.site.register(UploadVideo, UploadVideoAdmin)
