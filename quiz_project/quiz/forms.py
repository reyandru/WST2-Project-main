from django import forms
from django.core.exceptions import ValidationError
from .models import User  

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User 
        fields = ['username', 'password1', 'password2']  

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if ' ' in username:
            raise ValidationError('Username has no spaces.')
        return username

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            self.add_error('password2', 'Passwords do not match.')
