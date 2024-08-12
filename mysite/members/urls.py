from django.urls import path
from . import views


urlpatterns = [
    path("sign-up/", views.register_view, name="sign_up"),
    path("login/", views.login_view, name="login"),
]
