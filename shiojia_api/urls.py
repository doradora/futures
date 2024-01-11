from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("account/", views.trendAccount, name="account"),
    path("own_positions/", views.get_positions, name="positions"),
]