from django.shortcuts import render
from django.views.generic import CreateView
from .models import RolePlayingRoom
from .forms import RolePlayingRoomForm


class RolePlayingRoomCreateView(CreateView):
    model = RolePlayingRoom
    form_class = RolePlayingRoomForm


role_playing_room_new = RolePlayingRoomCreateView.as_view()
