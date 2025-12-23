from django.db import models
from django.contrib.auth.models import AbstractUser

class Group(models.Model):
    name = models.CharField(max_length=256)
    about = models.TextField(blank=True, null=True)

    @property # это чтобы можно было обращаться к функции без скобок
    def members_count(self):
        return self.members.count()

    # это как по дефолту будет отображаться обьект класса
    def __str__(self):
        return self.name

    # это как админ панель будет обращаться к классу
    class Meta:
        verbose_name = "Group"
        verbose_name_plural = "Group"

class CustomUser(AbstractUser):
    age = models.IntegerField()
    gender = models.CharField(max_length=30)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL,
                              null=True, blank=True, related_name="members")
    # это чтобы при создании супер юзера потребовались новые поля
    REQUIRED_FIELDS = ["age", "gender"]

    # это как админ панель будет обращаться к классу
    class Meta:
        verbose_name = "CmUser"
        verbose_name_plural = "CmUsers"

    # это как по дефолту будет отображаться обьект класса
    def __str__(self):
        return self.username
