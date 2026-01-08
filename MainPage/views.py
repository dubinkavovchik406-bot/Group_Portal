from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect, get_object_or_404

from MainPage import forms
from .mixins import UserIsOwnerMixin, AdminRequiredMixin, GroupModeratorEditMixin
from .models import Group, CustomUser
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login


class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True
    next_page = reverse_lazy('group-list')

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')

class RegisterView(FormView):
    template_name = 'users/register.html'
    form_class = forms.CustomUserCreationForm
    success_url = reverse_lazy('group-list')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

class GroupListView(LoginRequiredMixin, ListView):
    # це списки "груп" людей
    model = Group
    template_name = "groups/group_list.html"
    context_object_name = "groups_objects"

class GroupDetailView(LoginRequiredMixin, DetailView):
    # це для 1 конкретної групи
    model = Group
    template_name = "groups/group_detail.html"
    context_object_name = "group_object"

class GroupCreateView(LoginRequiredMixin, AdminRequiredMixin, CreateView):
    # створення групи
    model = Group
    form_class = forms.GroupForm
    template_name = "groups/group_form.html"
    context_object_name = "group_object"
    success_url = reverse_lazy("group-list")

class GroupUpdateView(LoginRequiredMixin, GroupModeratorEditMixin, UpdateView):
    model = Group
    form_class = forms.GroupForm
    template_name = "groups/group_form.html"
    context_object_name = "group_object"
    success_url = reverse_lazy("group-list")

class GroupDeleteView(LoginRequiredMixin, AdminRequiredMixin, DeleteView):
    model = Group
    success_url = reverse_lazy("group-list")
    template_name = "groups/group_delete.html"
    context_object_name = "group_object"

class JoinGroupView(LoginRequiredMixin, View):
    def post(self, request, pk):
        group = get_object_or_404(Group, pk=pk)
        user = self.request.user

        # Если юзер уже в какой-то группе, и он там был модером — сбрасываем роль
        if user.is_moderator:
            user.role = CustomUser.ROLE_USER

        # Меняем группу юзеру
        user.group = group
        user.save()

        return redirect("group-detail", pk=pk)

class LeaveGroupView(LoginRequiredMixin, View):
    def post(self, request, pk):
        group = get_object_or_404(Group, pk=pk)
        user = self.request.user

        # Проверяем, что юзер выходит именно из своей группы
        if user.group == group:
            # Сбрасываем роль модератора при выходе
            if user.is_moderator:
                user.role = CustomUser.ROLE_USER

            user.group = None
            user.save()

        return redirect('group-detail', pk=pk)


class UserUpdateView(LoginRequiredMixin, UserIsOwnerMixin, UpdateView):
    model = CustomUser
    form_class = forms.CustomUserUpdateForm
    template_name = "users/user_form.html"
    context_object_name = "user_object"

    def get_success_url(self):
        return reverse("user-detail", kwargs={"pk": self.object.pk})

class UserDeleteView(LoginRequiredMixin, UserIsOwnerMixin, DeleteView):
    model = CustomUser
    success_url = reverse_lazy("login")
    template_name = "users/user_delete.html"
    context_object_name = "user_object"

class UserListView(LoginRequiredMixin, AdminRequiredMixin, ListView):
    # список користувачів
    model = CustomUser
    template_name = "users/user_list.html"
    context_object_name = "users_objects"
    paginate_by = 3

class UserDetailView(LoginRequiredMixin, DetailView):
    # 1 користувач
    model = CustomUser
    template_name = "users/user_detail.html"
    context_object_name = "user_object"
