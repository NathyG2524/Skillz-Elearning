from django.forms import ModelForm
from .models import course
from .models import Section
from .models import Lesson


class CourseForm(ModelForm):
    class Meta:
        model = course
        fields = [ 'title', 'course_description', 'price', 'image']
    
    def __init__(self, *args, **kwargs):
        super(CourseForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class' : 'input'})

class SectionForm(ModelForm):
    class Meta:
        model = Section
        fields = [ 'title' ]
        widgets = {
            'tagfield': (),
        }
    
    def __init__(self, *args, **kwargs):
        super(SectionForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class' : 'input'})

class LessonForm(ModelForm):
    class Meta:
        model = Lesson
        fields = [ 'title', 'video']

    def __init__(self, *args, **kwargs):
        super(LessonForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class' : 'input'})
