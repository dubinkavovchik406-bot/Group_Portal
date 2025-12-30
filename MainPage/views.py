from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy, reverse

from .forms import CustomUserForm
from .models import Group, CustomUser
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

class CustomLoginView(LoginView):
    template_name = 'Group_portal/login.html'
    redirect_authenticated_user = True
    next_page = reverse_lazy('group-list')

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')

class RegisterView(FormView):
    template_name = 'Group_portal/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('group-list')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

class GroupListView(LoginRequiredMixin, ListView):
    # це списки "груп" людей
    model = Group
    template_name = "Group_portal/group_list.html"
    context_object_name = "groups"

class GroupDetailView(LoginRequiredMixin, DetailView):
    # це для 1 конкретної групи
    model = Group
    template_name = "Group_portal/group_detail.html"
    context_object_name = "group"

class GroupCreateView(LoginRequiredMixin, CreateView):
    # створення групи
    model = Group
    fields = ["name", "about"] #поля по моделям 
    template_name = "Group_portal/group_create.html"
    success_url = reverse_lazy("group-list")

class UserListView(LoginRequiredMixin, ListView):
    # список користувачів
    model = CustomUser
    template_name = "Group_portal/user_list.html"
    context_object_name = "users"

class UserDetailView(LoginRequiredMixin, DetailView):
    # 1 користувач
    model = CustomUser
    template_name = "Group_portal/user_detail.html"
    context_object_name = "user"

class GroupUpdateView(UpdateView):
    model = Group
    fields = ["name", "about"]
    template_name = "Group_portal/group_update.html"
    context_object_name = "group"
    success_url = reverse_lazy("group-list")

class GroupDeleteView(DeleteView):
    model = Group
    success_url = reverse_lazy("group-list")
    template_name = "Group_portal/group_delete.html"


class UserCreateView(CreateView):
    model = CustomUser
    form_class = CustomUserForm #Это подтягивает фиелдс Модели, но как отдельно оформленый класс
    success_url = reverse_lazy("user-list")
    template_name = "Group_portal/user_create.html"

class UserUpdateView(UpdateView):
    model = CustomUser
    form_class = CustomUserForm
    template_name = "Group_portal/user_update.html"

    def get_success_url(self):
        return reverse("user-detail", kwargs={"pk": self.object.pk})

class UserDeleteView(DeleteView):
    model = CustomUser
    success_url = reverse_lazy("user-list")
    template_name = "Group_portal/user_delete.html"

