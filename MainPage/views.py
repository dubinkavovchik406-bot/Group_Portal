from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Group, CustomUser

class GroupListView(ListView):
    # це списки "груп" людей
    model = Group
    template_name = "templates/GroupPortal/group_list.html"
    context_object_name = "groups"

class GroupDetailView(DetailView):
    # це для 1 конкретної групи
    model = Group
    template_name = "groups/group_detail.html"
    context_object_name = "group"

class GroupCreateView(CreateView):
    # створення групи
    model = Group
    fields = ["name", "about"] #поля по моделям 
    template_name = "groups/group_create.html"
    success_url = reverse_lazy("group-list")

class UserListView(ListView):
    # список користувачів
    model = CustomUser
    template_name = "users/user_list.html"
    context_object_name = "users"

class UserDetailView(DetailView):
    # 1 користувач
    model = CustomUser
    template_name = "users/user_detail.html"
    context_object_name = "user"

