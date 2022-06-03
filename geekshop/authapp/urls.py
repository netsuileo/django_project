import authapp.views as authapp
from django.urls import path

app_name = "authapp"

urlpatterns = [
    path("login/", authapp.login, name="login"),
    path("register/", authapp.register, name="register"),
    path("edit/", authapp.edit, name="edit"),
    path("logout/", authapp.logout, name="logout"),
    path("verify/<str:email>/<str:key>", authapp.verify, name="verify"),
]
