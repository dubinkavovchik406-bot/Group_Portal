
from django import forms
from .models import CustomUser, Group
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta): # Унаследует от базового класса пароли
        model = CustomUser
        fields = ("username","email",)

class CustomUserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ["email", "first_name", "last_name", "age", "gender"]

class JoinGroupForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ("group", )


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ["name", "about"]