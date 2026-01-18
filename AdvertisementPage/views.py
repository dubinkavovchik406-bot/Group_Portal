from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from .forms import AdvertisementForm
from .models import Advertisement
from MainPage import mixins as mp_mixins

class AdvertisementListView(LoginRequiredMixin, ListView):
    model = Advertisement
    template_name = "advertisement/advertisement-list.html"
    context_object_name = "advertisement_objects"

class AdvertisementCreateView(LoginRequiredMixin, mp_mixins.AdminRequiredMixin, CreateView):
    model = Advertisement
    form_class = AdvertisementForm
    template_name = "advertisement/advertisement-create.html"
    context_object_name = "advertisement_object"
    success_url = reverse_lazy("advertisement-list")

class AdvertisementUpdateView(LoginRequiredMixin, mp_mixins.AdminRequiredMixin, UpdateView):
    model = Advertisement
    form_class = AdvertisementForm
    template_name = "advertisement/advertisement-update.html"
    context_object_name = "advertisement_object"
    success_url = reverse_lazy("advertisement-list")

class AdvertisementDeleteView(LoginRequiredMixin, mp_mixins.AdminRequiredMixin, DeleteView):
    model = Advertisement
    template_name = "advertisement/advertisement-delete.html"
    context_object_name = "advertisement_object"
    success_url = reverse_lazy("advertisement-list")

class AdvertisementDetailView(LoginRequiredMixin, DetailView):
    model = Advertisement
    template_name = "advertisement/advertisement-detail.html"
    context_object_name = "advertisement_object"

