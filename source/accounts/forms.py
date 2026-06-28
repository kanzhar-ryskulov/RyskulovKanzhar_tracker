from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ['username', 'password1', 'password2',
                  'first_name', 'last_name', 'email']

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if not first_name or first_name.strip() == '':
            raise ValidationError('First name обязателен')
        return first_name

    def clean_email(self):
        email = self.cleaned_data['email']

        if not email or email.strip() == '':
            raise ValidationError('Введите почту')



