from django.urls import re_path

from .channels.chatconsumer import ChatConsumer
from .channels.gameconsumer import GameConsumer


websocket_urlpatterns = [
    re_path(r'ws/chess/match/(?P<match_id>\w+)/chat/$', ChatConsumer.as_asgi()),
    re_path(r'ws/chess/match/(?P<match_id>\w+)/game/$', GameConsumer.as_asgi())

]
# http://127.0.0.1:8000/chess/match/matchid