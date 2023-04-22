from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/chess/match/(?P<match_id>\w+)/$',consumers.GameRoomConsumer.as_asgi())
]

# http://127.0.0.1:8000/chess/match/matchid