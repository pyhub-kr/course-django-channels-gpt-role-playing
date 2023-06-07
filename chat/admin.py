from django.contrib import admin
from .models import RolePlayingRoom
from .forms import RolePlayingRoomForm


@admin.register(RolePlayingRoom)
class RolePlayingRoomAdmin(admin.ModelAdmin):
    form = RolePlayingRoomForm

    def save_model(self, request, obj, form, change):
        if change is False and form.is_valid():
            obj.user = request.user

        super().save_model(request, obj, form, change)
