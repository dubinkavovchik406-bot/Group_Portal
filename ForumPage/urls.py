from django.urls import path
from .views import (
    CommentListView,
    CommentDetailView,
    CommentCreationView,
    CommentUpdateView,
    CommentDeleteView,
    CommentLikeToggle,
)
# хз базові юрли
urlpatterns = [
    path("", CommentListView.as_view(), name="comment-list"),
    path("create/", CommentCreationView.as_view(), name="comment-create"),
    path("<int:pk>/", CommentDetailView.as_view(), name="comment-detail"),
    path("edit/<int:pk>/", CommentUpdateView.as_view(), name="comment-update"),
    path("delete/<int:pk>", CommentDeleteView.as_view(), name="comment-delete"),
    path("like/<int:pk>/", CommentLikeToggle.as_view(), name="comment-like"),
]
