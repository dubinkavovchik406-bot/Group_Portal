
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Проходим циклом по всем полям и добавляем им нужные классы
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control btn-round-sm border-2',
                'placeholder': field.label # добавим плейсхолдеры вместо пустых полей
            })


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ["name", "about"]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control shadow-sm',
                'placeholder': 'Наприклад: Любителі котів'
            }),
            'about': forms.Textarea(attrs={
                'class': 'form-control shadow-sm',
                'rows': 5,
                'placeholder': 'Розкажіть про що ваша спільнота...',
                'style': 'resize: none;'
            }),
        }
        labels = {
            'name': 'Назва спільноти',
            'about': 'Про групу',
        }