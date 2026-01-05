from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy, reverse

from MainPage import forms
from .mixins import UserIsOwnerMixin, IsStaffMixin
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
    context_object_name = "groups"

class GroupDetailView(LoginRequiredMixin, DetailView):
    # це для 1 конкретної групи
    model = Group
    template_name = "groups/group_detail.html"
    context_object_name = "group"

class GroupCreateView(LoginRequiredMixin, IsStaffMixin, CreateView):
    # створення групи
    model = Group
    form_class = forms.GroupForm
    template_name = "groups/group_create.html"
    success_url = reverse_lazy("group-list")

class GroupUpdateView(LoginRequiredMixin, IsStaffMixin, UpdateView):
    model = Group
    form_class = forms.GroupForm
    template_name = "groups/group_update.html"
    context_object_name = "group"
    success_url = reverse_lazy("group-list")

class GroupDeleteView(LoginRequiredMixin, IsStaffMixin, DeleteView):
    model = Group
    success_url = reverse_lazy("group-list")
    template_name = "groups/group_delete.html"

class JoinGroupView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = forms.JoinGroupForm
    template_name = "users/join_group.html"
    success_url = reverse_lazy("group-list")

    # Юзер может менять группу только самому себе(Кто бы ни зашел на эту страницу, всегда доставай из базы того, кто сейчас авторизован)
    def get_object(self, queryset=None):
        return self.request.user

class UserUpdateView(LoginRequiredMixin, UserIsOwnerMixin, UpdateView):
    model = CustomUser
    form_class = forms.CustomUserUpdateForm
    template_name = "users/user_update.html"

    def get_success_url(self):
        return reverse("user-detail", kwargs={"pk": self.object.pk})

class UserDeleteView(LoginRequiredMixin, UserIsOwnerMixin, DeleteView):
    model = CustomUser
    success_url = reverse_lazy("user-list")
    template_name = "users/user_delete.html"

class UserListView(LoginRequiredMixin, ListView):
    # список користувачів
    model = CustomUser
    template_name = "users/user_list.html"
    context_object_name = "users"

class UserDetailView(LoginRequiredMixin, DetailView):
    # 1 користувач
    model = CustomUser
    template_name = "users/user_detail.html"
    context_object_name = "user"

