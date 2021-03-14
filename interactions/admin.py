from django.contrib import admin

from interactions.models import Interaction


@admin.register(Interaction)
class InteractionAdmin(admin.ModelAdmin):
    pass
