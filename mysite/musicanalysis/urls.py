from django.urls import path

from . import views

app_name = "musicanalysis"

urlpatterns = [
    path("", views.top, name="top"),
]