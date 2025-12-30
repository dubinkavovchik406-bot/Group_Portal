from django.urls import path
from .views import (
    GroupListView, GroupDetailView, GroupCreateView, GroupUpdateView,
    UserListView, UserDetailView, GroupDeleteView, UserCreateView, UserUpdateView, UserDeleteView, 
    CustomLoginView, CustomLogoutView, RegisterView
)

urlpatterns = [
    path("", CustomLoginView.as_view(), name="login"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("register/", RegisterView.as_view(), name="register"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),

    path("groups/", GroupListView.as_view(), name="group-list"),
    path("groups/create/", GroupCreateView.as_view(), name="group-create"),
    path("groups/<int:pk>/", GroupDetailView.as_view(), name="group-detail"),
    path("groups/update/<int:pk>/", GroupUpdateView.as_view(), name="group-update"),
    path("groups/delete/<int:pk>/", GroupDeleteView.as_view(), name="group-delete"),

    path("users/", UserListView.as_view(), name="user-list"),
    path("users/<int:pk>/", UserDetailView.as_view(), name="user-detail"),
    path("users/create/", UserCreateView.as_view(), name="user-create"),
    path("users/update/<int:pk>/", UserUpdateView.as_view(), name="user-update"),
    path("users/delete/<int:pk>/", UserDeleteView.as_view(), name="user-delete"),
]
