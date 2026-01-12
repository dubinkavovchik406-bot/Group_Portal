from django.contrib.auth.mixins import UserPassesTestMixin
from MainPage.models import CustomUser


class UserIsOwnerMixin(UserPassesTestMixin):
    # Выкидывает ошибку форбиден 403
    raise_exception = True
    # Должна вернуть True(Доступ разрешён) или False(доступ не разрешён)
    def test_func(self):
        # Получаем юзера, который пытается воспользоваться вью с этой миксиной
        obj = self.get_object()
        user = self.request.user

        # Проверяем, является ли текущий юзер самим CustomUser
        if isinstance(obj, CustomUser):
            # сравниваем, это тот же человек, который залогинен?
            return obj == user
        # У этого обьекта есть поле автор?(для комментария)
        if hasattr(obj, "author"):
            # сравниваем(для комментария), это тот же человек, который залогинен?
            return obj.author == user

        return False

class AdminRequiredMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        user = self.request.user
        # Просто проверяет есть нужная(админ) роль в поле role текущего юзера или суперюзер(что по факту делает админом)
        return user.role == CustomUser.ROLE_ADMIN or user.is_superuser

# Приминяется к группе, дабы проверить чтобы к этой ГРУППЕ имел доступ админ/модератор самой группы
class GroupModeratorEditMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        user = self.request.user
        group_obj = self.get_object()

        is_admin = (user.role == CustomUser.ROLE_ADMIN or user.is_superuser)
        is_my_group_moderator = (user.role == CustomUser.ROLE_MODERATOR and user.group == group_obj)

        return is_admin or is_my_group_moderator