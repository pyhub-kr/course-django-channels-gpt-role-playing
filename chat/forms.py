from django import forms
from .models import RolePlayingRoom


class RolePlayingRoomForm(forms.ModelForm):
    class Meta:
        model = RolePlayingRoom
        fields = "__all__"
