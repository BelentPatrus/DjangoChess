from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from corechannels.routing import websocket_urlpatterns
from django.core.asgi import get_asgi_application
django_asgi_app = get_asgi_application()
application = ProtocolTypeRouter({
    "http": django_asgi_app,
    'websocket' : AuthMiddlewareStack(
        URLRouter(websocket_urlpatterns)
    ),
})
