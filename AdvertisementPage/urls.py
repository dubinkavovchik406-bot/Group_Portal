from django.urls import path

from .views import (AdvertisementListView,
                    AdvertisementCreateView,
                    AdvertisementDeleteView,
                    AdvertisementUpdateView,
                    AdvertisementDetailView)

urlpatterns = [
    path("", AdvertisementListView.as_view(), name="advertisement-list"),
    path("create/", AdvertisementCreateView.as_view(), name="advertisement-create"),
    path("update/<int:pk>/", AdvertisementUpdateView.as_view(), name="advertisement-update"),
    path("delete/<int:pk>/", AdvertisementDeleteView.as_view(), name="advertisement-delete"),
    path("detail/<int:pk>/", AdvertisementDetailView.as_view(), name="advertisement-detail"),
]