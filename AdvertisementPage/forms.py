from django import forms
from .models import Advertisement

class AdvertisementForm(forms.ModelForm):
    class Meta:
        model = Advertisement
        fields = ["name", "about", "media", "youtube_url"]
        labels = {
            'name': 'Заголовок оголошення',
            'about': 'Опис / Текст',
            'media': 'Завантажити файл (фото/відео)',
            'youtube_url': 'Посилання на YouTube (якщо є)',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Автоматически добавляем класс Bootstrap каждому полю
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})