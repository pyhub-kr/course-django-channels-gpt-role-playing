from django import forms
from .models import RolePlayingRoom
from .translators import google_translate


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

    def clean(self):
        situation = self.cleaned_data.get("situation")
        situation_en = self.cleaned_data.get("situation_en")
        if situation and not situation_en:
            self.cleaned_data["situation_en"] = self._translate(situation)

        my_role = self.cleaned_data.get("my_role")
        my_role_en = self.cleaned_data.get("my_role_en")
        if my_role and not my_role_en:
            self.cleaned_data["my_role_en"] = self._translate(my_role)

        gpt_role = self.cleaned_data.get("gpt_role")
        gpt_role_en = self.cleaned_data.get("gpt_role_en")
        if gpt_role and not gpt_role_en:
            self.cleaned_data["gpt_role_en"] = self._translate(gpt_role)

        return self.cleaned_data

    @staticmethod
    def _translate(origin_text: str) -> str:
        translated = google_translate(origin_text, "auto", "en")
        if not translated:
            raise forms.ValidationError("구글 번역에 실패했습니다.")
        return translated
