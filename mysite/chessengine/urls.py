from django.urls import path
from . import views


urlpatterns = [
    path('', views.lobby, name="lobby"),
    path('match/<str:match_id>', views.chessMatch, name="match"),
    path('getData/', views.getData, name="getData"),
    path('latestBoard/<int:gameStateId>', views.getLatestChessBoardData, name="latestBoard"),
    path('processClick/', views.processClick, name="processClick")
]
