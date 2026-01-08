
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator

class Group(models.Model):
    name = models.CharField(max_length=25, unique=True,
                            validators=[MinLengthValidator(3, message="Назва групи має містити принаймні 3 символи")])
    about = models.TextField(blank=True, null=True)

    @property # это чтобы можно было обращаться к функции без скобок
    def members_count(self):
        return self.members.count()

    # это как по дефолту будет отображаться объект класса
    def __str__(self):
        return self.name

    # это как админ панель будет обращаться к классу
    class Meta:
        verbose_name = "Group"
        verbose_name_plural = "Groups"

class CustomUser(AbstractUser):
    ROLE_USER = "user"
    ROLE_MODERATOR = "moderator"
    ROLE_ADMIN = "admin"

    GENDER_FEMALE = "female"
    GENDER_MALE = "male"

    # То из чего выбирать
    ROLE_CHOICES = [
        (ROLE_USER, "Користувач"),
        (ROLE_MODERATOR, "Модератор"),
        (ROLE_ADMIN, "Адміністратор")
    ]

    GENDER_CHOICES = [
        (GENDER_MALE, "Чоловік"),
        (GENDER_FEMALE, "Жінка")
    ]

    age = models.IntegerField(null=True, blank=True)
    # choices - вместо ручной прописи, выбираешь из вариантов
    gender = models.CharField(max_length=30, choices=GENDER_CHOICES, null=True, blank=True)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL,
                              null=True, blank=True, related_name="members")
    role = models.CharField(max_length=20, choices=ROLE_CHOICES,
                            default=ROLE_USER)

    # это чтобы при создании супер юзера потребовались новые поля, gender = male/female
    REQUIRED_FIELDS = ["age", "gender"]

    # это как админ панель будет обращаться к классу
    class Meta:
        verbose_name = "CmUser"
        verbose_name_plural = "CmUsers"

    # это как по дефолту будет отображаться объект класса
    def __str__(self):
        return self.username

    # Теперь, чтобы проверить юзер это админ или нет, можно просто написать user.is_admin
    @property
    def is_admin(self):
        return self.role == self.ROLE_ADMIN or self.is_superuser

    # Теперь, чтобы проверить юзер это модер или нет, можно просто написать user.is_moderator
    @property
    def is_moderator(self):
        return self.role == self.ROLE_MODERATOR

    def is_my_group_moderator(self, group_obj):
        return self.is_moderator and self.group == group_obj
