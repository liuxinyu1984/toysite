from django import forms
from courses.models import Lecture


class CreateLectureForm(forms.ModelForm):
    class Meta:
        model = Lecture
        fields = '__all__'
        widgets = {
            'course': forms.widgets.Select(attrs={
                'readonly': True,
                'disabled': True
            }),
            'title': forms.TextInput(),
            'week': forms.NumberInput(),
            'syllabus': forms.Textarea(),
            'is_midterm': forms.CheckboxInput(),
            'is_final': forms.CheckboxInput(),
        }
