from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import re

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        max_length=30,
        min_length=3,
        help_text='Required. 3-30 characters. Letters and digits only.',
        widget=forms.TextInput(attrs={'placeholder': 'Username'})
    )

    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.match(r'^[\w.@+-]+$', username):
            raise forms.ValidationError('Username can only contain letters, numbers, and @/./+/-/_')
        return username

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email')
