from django.contrib import admin
from .models import Character, Player


class PlayerAdmin(admin.ModelAdmin):
    list_display = ['name', 'id', 'step']


admin.site.register(Character)
admin.site.register(Player, PlayerAdmin)
