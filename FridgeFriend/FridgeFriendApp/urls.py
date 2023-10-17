from django.urls import path
from . import views

urlpatterns = [
    path("index/", views.index, name="index"),
    path("", views.signin),
    path("index/addrecord/", views.addrecord, name="addrecord"),
    path("index/deleterecord/<int:id>", views.deleterecord, name="deleterecord"),
    path("index/updaterecord/<int:id", views.updaterecord, name="updaterecord")
]
