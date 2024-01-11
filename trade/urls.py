from django.urls import path

from . import views

urlpatterns = [
    path("order/",views.fut_order, name="order")
]