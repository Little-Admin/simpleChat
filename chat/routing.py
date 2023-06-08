from django.urls import re_path, path
from chat.consumers import chatConsumer
 
# Here, "" is routing to the URL ChatConsumer which
# will handle the chat functionality.
"""
websocket_urlpatterns = [
    path("" , ChatConsumer.as_asgi()) ,
]
"""

websocket_urlpatterns = [
    path('ws/c/<str:friends_room>', chatConsumer.as_asgi())
]