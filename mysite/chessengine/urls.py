from django.urls import path
from . import views


urlpatterns = [
    path('', views.lobby, name="lobby"),
    path('match/<str:match_id>', views.chessMatch, name="match"),

    path('getData/', views.getData, name="getData"),
    path('postData/', views.twoPointMove, name="postData"),
    path('latestBoard/<int:gameStateId>',
         views.getLatestChessBoardData, name="latestBoard"),


]
