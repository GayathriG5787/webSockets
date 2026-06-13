# path() is used for simple urls, while re_path uses regular expressions for complex URL patterns 

from django.urls import path
from .consumers import ChatConsumer

websocket_urlpatterns = [
    path('ws/socket-server/', ChatConsumer.as_asgi()),
]