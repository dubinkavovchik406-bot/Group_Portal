from django.urls import path
from .views import (
    GroupListView, GroupDetailView, GroupCreateView,
    UserListView, UserDetailView
)

#думаю не треба пояснювать що це
urlpatterns = [
    path("groups/", GroupListView.as_view(), name="group-list"),
    path("groups/create/", GroupCreateView.as_view(), name="group-create"),
    path("groups/<int:pk>/", GroupDetailView.as_view(), name="group-detail"),

    path("users/", UserListView.as_view(), name="user-list"),
    path("users/<int:pk>/", UserDetailView.as_view(), name="user-detail"),
]
