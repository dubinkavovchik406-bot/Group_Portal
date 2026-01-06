
from django.contrib.auth.mixins import UserPassesTestMixin
from MainPage.models import CustomUser


class UserIsOwnerMixin(UserPassesTestMixin):
    # Должна вернуть True(Доступ разрешён) или False(доступ не разрешён)
    def test_func(self):
        # Получаем юзера, который пытается воспользоваться вью с этой миксиной
        obj = self.get_object()

        # Проверяем, является ли текущий юзер самим CustomUser
        if isinstance(obj, CustomUser):
            # сравниваем, это тот же человек, который залогинен?
            return obj == self.request.user
        # сравниваем(для комментария), это тот же человек, который залогинен?
        return obj.author == self.request.user

class IsStaffMixin(UserPassesTestMixin):
    # Должна вернуть True(Доступ разрешён) или False(доступ не разрешён)
    def test_func(self):
        # Просто проверяет есть нужная(админ/модер) роль в поле role текущего юзера
        return self.request.user.role in [CustomUser.ROLE_ADMIN, CustomUser.ROLE_MODERATOR]