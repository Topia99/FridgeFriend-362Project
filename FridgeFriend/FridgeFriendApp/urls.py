from django.urls import path, include
from rest_framework import routers
from . import views

# router = routers.DefaultRouter()
# router.register('', views.ItemViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
# ]



urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.signin),
    path("index/addrecord/", views.addrecord, name="addrecord"),
    path("index/deleterecord/<int:id>", views.deleterecord, name="deleterecord"),
    path("index/updaterecord/<int:id", views.updaterecord, name="updaterecord")
]
