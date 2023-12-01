from django.urls import path, include
from . import views

# router = routers.DefaultRouter()
# router.register('', views.ItemViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
#     path('login', views.login),
#     path('signup', views.signup),
#     path('test_token', views.test_token),
#     path('accounts/', include("django.contrib.auth.urls")),
# ]



urlpatterns = [
    path("fridge/<uuid:pk>", views.index, name="fridge"),
    path("login/", views.loginPage, name='login'),
    path("logout/", views.logoutUser, name='logout'),
    path("register/", views.registerPage, name='register'),
    path("addrecord/<uuid:pk>", views.addrecord, name="addrecord"),
    path("fridge/<uuid:pk>/deleterecord/<int:id>", views.deleterecord, name="deleterecord"),
    path("updaterecord/<uuid:id>", views.updaterecord, name="updaterecord"),
    path("create_fridge/", views.createFridge, name="createFridge"),
    path("", views.userProfile, name='user'),
]
