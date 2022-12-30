from django.urls import path
from . import views


urlpatterns = [
    path('getData/', views.getData, name="getData"),
    path('postData/', views.twoPointMove, name="postData"),

]
