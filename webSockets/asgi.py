"""
ASGI config for webSockets project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
# ProtocolTypeRouter Routes incoming connections based on the protocol type (HTTP or Web Socket)
# URLRouter routes incoming web socket connections to the correct consumer (similar to urlpatterns routes HTTP requests to views)
from channels.routing import ProtocolTypeRouter, URLRouter

# AuthMiddleware requires SessionMiddleware, which requires CookieMiddleware. These 3 are combined in AuthMiddlewareStack
# It is used to make the logged-in user available inside the web socket consumer.
# Done by reading the user's session cookie and attaching the user in the connection scope dictionary
from channels.auth import AuthMiddlewareStack
import chat.routing


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webSockets.settings')

application = ProtocolTypeRouter({
    # get_asgi_application creates connection between web server and django project
    #If the incoming connection is an HTTP request, send it to Django's normal request handling system
    
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    )
})
