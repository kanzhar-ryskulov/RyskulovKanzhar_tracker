from django import forms
from tracker_app.models import Task, Type, Status


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('summary', 'description', 'status', 'type')
        widgets = {
            'summary': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
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
