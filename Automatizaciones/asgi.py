"""
ASGI config for Automatizaciones project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
import medios_magneticos.routing  # Nuevo archivo con rutas

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Automatizaciones.settings')

application = get_asgi_application()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tu_proyecto.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            medios_magneticos.routing.websocket_urlpatterns
        )
    ),
})
