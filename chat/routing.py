from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path("ws/chat/<int:room_pk>/", consumers.RolePlayingRoomConsumer.as_asgi()),
]
