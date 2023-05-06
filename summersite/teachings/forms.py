from django import forms
from courses.models import Lecture, UploadNote, UploadVideo


class CreateLectureForm(forms.ModelForm):

    class Meta:
        model = Lecture
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CreateLectureForm, self).__init__(*args, **kwargs)
        self.fields['course'].disabled = True


class CreateNoteForm(forms.ModelForm):

    class Meta:
        model = UploadNote
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CreateNoteForm, self).__init__(*args, **kwargs)
        self.fields['lecture'].disabled = True
