from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.contrib.auth import get_user_model
from django.core import validators
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('first_name','last_name','email','username','address','image','user_type1')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        validators.validate_email(email)

        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists")
        return email  