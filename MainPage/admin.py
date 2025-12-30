from django.contrib import admin
from .models import CustomUser, Group

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    # Какие поля отображать в списке
    list_display = ("username", "is_staff")
    # По каким полям можно искать
    search_fields = ("username", "")
    # Фильтры справа
    list_filter = ("is_staff", "is_superuser")

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ("name", "members_count")