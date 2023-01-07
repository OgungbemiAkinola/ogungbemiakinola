from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("tsietsi", views.page1, name="page1"),
    path("impossible", views.page2, name="page2"),
    path("ghost", views.page3, name="page3"),
    path("sovenga", views.page4, name="page4"),
    path("motho", views.page5, name="page5")
]