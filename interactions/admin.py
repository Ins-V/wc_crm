from django.contrib import admin

from interactions.models import Keyword, Interaction


@admin.register(Interaction)
class InteractionAdmin(admin.ModelAdmin):
    list_select_related = ('company',)


admin.site.register(Keyword)
