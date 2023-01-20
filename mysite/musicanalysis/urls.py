from django.urls import path

from . import views

app_name = "musicanalysis"

urlpatterns = [
    path("", views.top, name="top"),
    path("result/", views.result, name="result"),
    path("hist/", views.get_svg, name="hist"),
    path("heat/", views.get_heat, name="heat"),
]