from pprint import pprint
from typing import List

from channels.generic.websocket import JsonWebsocketConsumer
from django.contrib.auth.models import AbstractUser

from chat.models import RolePlayingRoom, GptMessage


class RolePlayingRoomConsumer(JsonWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.gpt_messages: List[GptMessage] = []

    def connect(self):
        room = self.get_room()
        if room is None:
            self.close()
        else:
            self.accept()

            self.gpt_messages = room.get_initial_messages()
            print(self.gpt_messages)

    def receive_json(self, content, **kwargs):
        # Echo
        self.send_json(content)

    def get_room(self) -> RolePlayingRoom | None:
        user: AbstractUser = self.scope["user"]
        room_pk = self.scope["url_route"]["kwargs"]["room_pk"]
        room: RolePlayingRoom = None

        if user.is_authenticated:
            try:
                room = RolePlayingRoom.objects.get(pk=room_pk, user=user)
            except RolePlayingRoom.DoesNotExist:
                pass

        return room
