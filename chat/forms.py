from django import forms
from .models import RolePlayingRoom


class RolePlayingRoomForm(forms.ModelForm):
    class Meta:
        model = RolePlayingRoom
        fields = [
            "language",
            "level",
            "situation",
            "situation_en",
            "my_role",
            "my_role_en",
            "gpt_role",
            "gpt_role_en",
        ]
