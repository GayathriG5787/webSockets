"""
ASGI config for webSockets project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os
from channels.routing import ProtocolTypeRouter
# Routes incoming connections based on the protocol type (HTTP or Web Socket)
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webSockets.settings')

application = ProtocolTypeRouter({
    # get_asgi_application creates connection between web server and django project
    #If the incoming connection is an HTTP request, send it to Django's normal request handling system
    
    'http': get_asgi_application()
})
