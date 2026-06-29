from django import forms
from tracker_app.models import Task, Type, Status, Project


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('summary', 'description', 'type',)
        widgets = {
            'summary': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'type': forms.CheckboxSelectMultiple(),
        }


class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = '__all__'


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = '__all__'

class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label='')

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project

        fields = ('start_date', 'end_date','title', 'description', )
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }
