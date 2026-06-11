from django import forms
from tracker_app.models import Task, Type, Status


class TaskForm(forms.ModelForm):
    summary = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    status = forms.ModelChoiceField(queryset=Status.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Task
        fields = '__all__'
        exclude = ('created_at', 'updated_at')
        widgets = {
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
