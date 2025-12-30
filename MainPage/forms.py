from django import forms
from .models import CustomUser, Group
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = (
            "username",
            "age",
            "gender",
            "group",
            "password1",
            "password2",
        )
        
class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ["name", "about"]

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ["username", "first_name", "last_name", "age", "gender", "email", "group"]
