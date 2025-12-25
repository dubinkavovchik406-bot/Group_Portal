from django import forms
from .models import CustomUser, Group

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ["name", "about"]

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ["username", "first_name", "last_name", "age", "gender", "email", "group"]
