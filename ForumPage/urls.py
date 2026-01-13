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
    path("<int:pk>/edit/", CommentUpdateView.as_view(), name="comment-update"),
    path("<int:pk>/delete/", CommentDeleteView.as_view(), name="comment-delete"),
    path("<int:pk>/like/", CommentLikeToggle.as_view(), name="comment-like"),
]
