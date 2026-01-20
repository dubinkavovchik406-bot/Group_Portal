from django.db import models

class Advertisement(models.Model):
    name = models.CharField(max_length=30)
    about = models.TextField()
    media = models.FileField(upload_to="advertisement/", blank=True, null=True)
    youtube_url = models.URLField(blank=True, null=True, verbose_name="Посилання на YouTube")

    def __str__(self):
        return f"Повідомлення: {self.name}"

    class Meta:
        verbose_name = "Advertisement"
        verbose_name_plural = "Advertisements"
