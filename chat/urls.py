from django.urls import path
from . import views

urlpatterns = [
    path("new/", views.role_playing_room_new, name="role_playing_room_new"),
]
