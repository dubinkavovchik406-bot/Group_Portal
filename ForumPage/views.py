from django.shortcuts import render
from .models import Comment, Like
from .mixins import UserIsOwnerMixin
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView, View
)
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# дивитись на всі коментарі
class CommentListView(LoginRequiredMixin, ListView):
    model = Comment
    template_name = "forum/comment_list.html"
    context_object_name = "comments"
    ordering = ["-created_at"]

# 1 коментар, а далі лінь коментаувати тому що там і так понятно що за в'юшки
class CommentDetailView(LoginRequiredMixin, DetailView):
    model = Comment
    template_name = "forumpage/comment_detail.html"
    context_object_name = "comment"

class CommentCreationView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ["content", "media"]
    template_name = "forumpage/comment_create.html"
    success_url = reverse_lazy("comment-list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class CommentUpdateView(LoginRequiredMixin, UserIsOwnerMixin, UpdateView):
    model = Comment
    fields = ["content", "media"]
    template_name = "forumpage/comment_update.html"

class CommentDeleteView(LoginRequiredMixin, UserIsOwnerMixin, DeleteView):
    model = Comment
    template_name = "forumpage/comment_delete.html"
    success_url = reverse_lazy("comment-list")

class CommentLikeToggle(LoginRequiredMixin, View):

    def post(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk)

        like, created = Like.objects.get_or_create(comment=comment, user=request.user)

        if not created:
            like.delete()

        return redirect("comment-detail", pk=pk)

