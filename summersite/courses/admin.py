from django.contrib import admin
from .models import Course, Lecture

#admin.site.register(Course)


class CourseAdmin(admin.ModelAdmin):

    def course_title(self, obj):
        return obj.subject + " " + obj.course_number

    def term_of_course(self, obj):
        return obj.course_year() + " " + obj.term.lower()
    
    list_display = ('course_title', 'term_of_course', 'section', 'instructor')
    #fields = ['subject', 'course_number', 'term', 'section', 'instructor', 'start_date', 'end_date']
    fieldsets = (
        ('Course', {'fields': ('subject', 'course_number', 'section')}),
        ('Time', {'fields': ('term', 'start_date', 'end_date')}),
        ('Instructor', {'fields': ('instructor',)})
    )
    ordering = ['subject', 'course_number', 'instructor']
    list_filter = ('subject', 'instructor')
    #search_fields = ['subject', 'instructor']

admin.site.register(Course, CourseAdmin)


class LectureAdmin(admin.ModelAdmin):

    # def course_title(self):
    #     return self.course.__str__()
    
    list_display = ('course', 'week', 'created_at', 'updated_at', 'is_midterm', 'is_final')
    #prepopulated_fields = {"slug": ['course', 'week']}

admin.site.register(Lecture, LectureAdmin)